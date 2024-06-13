# JD-JRS Mapping Bot

## Prerequisites
- **Python 3.x:** Ensure Python is installed. You can download it from [Python.org](https://www.python.org/downloads/).
- **pip:** Typically comes with Python. Verify installation by running pip --version in your terminal.
- **Microsoft Build Tools with C++:** Required for compiling some dependencies. Download and install from [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/). During installation, ensure to check the **"Desktop development with C++"** workload

## Setup
**1. Clone or Download the Project**
   - Clone the repository using git: 
   ```bash
   git clone https://github.com/nawin-viswajith/JD-JRS-MappingBot.git
   ```
   - Or download the project as a ZIP file from the repository and extract it.

**2. Navigate to the project directory**
   - Open your terminal or command prompt and navigate to the directory where you cloned or extracted the project
   ```bash
   cd JD-JRS-MappingBot/Streamlit_ChromaDB
   ```
**3. Download and prepare ChromaDB**
   - Download ChromaDB.zip: Ensure the file is available in the same directory as your project files. If not, download it from the specified location or repository.
   - Paste the ZIP file in the project directory if it's not already there.
   - Extract the ZIP file:
   ```bash
   unzip ChromaDB.zip
   ```
   This should create a ChromaDB folder with the necessary files inside.

**4. Extract the zip file in the same directory.**

**5. Install dependencies:**
   - Install required Python packages listed in **requirements.txt**:
   ```bash
   pip install -r requirements.txt
   ```

**6. Run the application:**
   - Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```
This will open a new tab in your web browser with the JD-JRS Mapping Bot interface.


## Usage
- Enter your query: In the provided text area, input your query (e.g., a job description or role).
- Click "Submit": The bot will process your query and display relevant results.


## Contributions
Contributions to the JD-JRS Mapping Bot project, particularly enhancements or optimizations for JD to JRS mapping, are highly encouraged. If you have suggestions for improvements or new features, feel free to:

   - Submit a pull request: Fork the repository, make your changes, and submit a pull request for review.
   - Open an issue: Use the repository’s issue tracker to report bugs or request features.

## License
This ChatBot is provided under the [MIT License](LICENSE). You are free to modify and distribute the code for your own purposes.
