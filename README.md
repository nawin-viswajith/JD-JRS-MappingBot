# ChatBot Readme - JD JRS Mapping

## Overview
This ChatBot is specifically tailored for the purpose of mapping Job Descriptions (JDs) to Job Role Summaries (JRS). It assists users in retrieving relevant information from JDs stored in an Excel file and provides corresponding JRS based on user queries. The ChatBot utilizes natural language processing techniques and pre-trained models to facilitate efficient mapping between JDs and JRS.

## Features
- **JD to JRS Mapping**: Users can input queries related to specific job roles or tasks, and the ChatBot retrieves corresponding JRS based on the information extracted from JDs.
- **Excel File Integration**: The ChatBot is integrated with an Excel file containing JDs, enabling seamless retrieval of information from structured data.
- **Graphical User Interface (GUI)**: The ChatBot interface is implemented using Tkinter, providing a user-friendly and intuitive experience for mapping JDs to JRS.

## Installation
1. Ensure you have Python installed on your system (Python 3.x recommended). You can download and install Python from the official website: [Python.org](https://www.python.org/downloads/). Choose the appropriate installer for your operating system and follow the installation instructions provided on the website.
3. Install the required libraries by running:
    ```
    pip install pandas numpy sentence-transformers scikit-learn chromadb tk
    ```
4. Clone or download the ChatBot source code from the repository.

## Usage
1. **Excel File Setup**:
    - Prepare an Excel file containing the JDs to be mapped to JRS. Each JD should be in a separate row.
    - Paste the path to the excel file in the command prompt window after running the python file or Update the `file_path` variable in the `excel_to_chunks()` function with the path to your Excel file if you want to set a default path.

2. **Run the ChatBot**:
    - Navigate to the directory containing the ChatBot source code.
    - Run the `chatbot.py` file using Python:
        ```
        python chatbot.py
        ```

3. **Interact with the ChatBot**:
    - The ChatBot GUI will open, displaying a chat history window and an input box.
    - Enter queries related to specific job roles or tasks into the input box and press Enter or click the "Enter" button.
    - The ChatBot will process your input, retrieve relevant information from JDs, and display the corresponding JRS in the chat history window.

4. **Clear Chat History**:
    - To clear the chat history, click the "Clear" button.

## Notes
- Ensure that the Excel file containing JDs is properly formatted and structured to facilitate accurate mapping to JRS.
- The ChatBot relies on pre-trained models for natural language processing and text embeddings. Additional training or fine-tuning may be necessary depending on specific use cases or requirements.

## Contributions
Contributions to the ChatBot project, particularly enhancements or optimizations for JD to JRS mapping, are encouraged. If you have suggestions for improvements or would like to contribute new features, please feel free to submit a pull request or open an issue on the repository.

## License
This ChatBot is provided under the [MIT License](LICENSE). You are free to modify and distribute the code for your own purposes.

## Credits
- Developed by Babu Ramraj Ramachandran.
- Utilizes pre-trained models from the [Sentence Transformers](https://github.com/UKPLab/sentence-transformers) library.
- Built using the Tkinter library for the graphical user interface.
