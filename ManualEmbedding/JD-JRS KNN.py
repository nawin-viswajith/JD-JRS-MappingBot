# Import necessary libraries
import warnings
import pandas as pd
import numpy as np

# Importing from specific modules
from chromadb.api.types import EmbeddingFunction
from sentence_transformers import SentenceTransformer
from sklearn.manifold import TSNE
from sklearn.neighbors import NearestNeighbors
from typing import Literal, Optional, Any

# Import TKinter for GUI
import tkinter as tk
from tkinter import scrolledtext

# Suppressing warnings
warnings.filterwarnings("ignore")

class ChatUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")

        # Adjust the width and height of the chat history text box
        self.chat_history = scrolledtext.ScrolledText(root, width=100, height=40, wrap=tk.WORD)
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.input_box = tk.Entry(root, width=70)
        self.input_box.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(root, text="Enter", width=5, command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=5, pady=10, sticky='w')

        self.clear_button = tk.Button(root, text="Clear", width=5, command=self.clear_chat)
        self.clear_button.grid(row=1, column=1, padx=20, pady=10, sticky='e')

        self.root.bind("<Return>", self.send_message)

        self.chat_history.insert(tk.END, "Welcome to the ChatBot!\n")
        self.chat_history.configure(state='disabled')

    def send_message(self, event=None):
        message = self.input_box.get()
        if message.strip() == "":
            return
        self.input_box.delete(0, tk.END)
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, "\nYou: " + message + "\n")

        # Pass user input to the model and get the output
        grouped_chunks = {}
        for idx in self.get_model_output(message):
            chunk = chunks[idx]
            chunk_type = chunk.split('-')[0].strip()
            chunk_description = chunk.split('-')[1].strip()
            if chunk_type not in grouped_chunks:
                grouped_chunks[chunk_type] = []
            grouped_chunks[chunk_type].append(chunk_description)

        # Display the neighboring chunks in the chat history
        self.chat_history.insert(tk.END, "\nBot: \n")
        for chunk_type, chunk_list in grouped_chunks.items():
            self.chat_history.insert(tk.END, "\t" + chunk_type.capitalize() + ":\n")
            for chunk in chunk_list:
                self.chat_history.insert(tk.END, "\t\t" + chunk + "\n")
        self.chat_history.configure(state='disabled')
        self.chat_history.see(tk.END)  # Scroll to the bottom

    def clear_chat(self):
        self.chat_history.configure(state='normal')
        self.chat_history.delete(1.0, tk.END)
        self.chat_history.configure(state='disabled')
        self.input_box.focus()

    def get_model_output(self, message):
        question = message
        emb_question = emb_function([question])

        # Create a t-SNE model
        tsne = TSNE(n_components=2, random_state=42)
        embeddings_with_question = np.vstack([embeddings, emb_question])
        embeddings_2d = tsne.fit_transform(embeddings_with_question)

        # Create a NearestNeighbors model for the original embeddings
        nn = NearestNeighbors(n_neighbors=5)
        nn.fit(embeddings_2d[:-1])

        # Find the nearest neighbors of the input question embedding
        neighbors = nn.kneighbors(embeddings_2d[-1].reshape(1, -1), return_distance=False)

        # Extract the indices of nearest neighbors as a list
        neighbors_list = neighbors.tolist()
        return neighbors_list[0]


def excel_to_chunks():
    chunks = []

    # Step 1: Read the Excel file
    file_path = input("Enter the path to the Excel file: ").strip("\"")
    # file_path = path_to_excel_file
    df = pd.read_excel(file_path, header=None)

    # Step 2: Convert each non-empty row into a chunk
    rag_chunks = {}
    for index, row in df.iloc[1:].iterrows():  # Skip the first row
        if not pd.isna(row[0]) and str(row[0]).strip() != "":
            rag_chunks.setdefault('Chunk', []).append(row[0])

    # Step 3: Print or further process the chunks
    for i, chunk in enumerate(rag_chunks['Chunk']):
        row_chunks = f"[Row {i + 1}]: {chunk}\n"  # Adjust row number due to skipping the first row
        chunks.append(row_chunks)

    return chunks


def get_text_embedding(texts: list[list[str]], batch: int = 1000) -> list[Any]:
    """
    Get the embeddings from the text.

    Args:
        texts (list[str]): List of chunks of text.
        batch (int): Batch size.
    """
    embeddings = []
    for i in range(0, len(texts), batch):
        text_batch = texts[i:(i + batch)]
        # Embeddings model
        emb_batch = emb_function(text_batch)
        embeddings.append(emb_batch)
    embeddings = np.vstack(embeddings)
    return embeddings


# Load the model from TF Hub
class MiniLML6V2EmbeddingFunction(EmbeddingFunction):
    MODEL = SentenceTransformer('all-MiniLM-L6-v2')

    def __call__(self, texts):
        return MiniLML6V2EmbeddingFunction.MODEL.encode(texts).tolist()


emb_function = MiniLML6V2EmbeddingFunction()

# Read Excel file and convert to chunks
chunks = excel_to_chunks()

# Get text embeddings
embeddings = get_text_embedding(chunks)

def main():
    root = tk.Tk()
    # Read Excel file and convert to chunks
    app = ChatUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
