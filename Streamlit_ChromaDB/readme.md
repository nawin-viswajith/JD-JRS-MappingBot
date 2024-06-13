# JD-JRS Mapping Bot

## Prerequisites
- Python 3.x: Ensure Python is installed. You can download it from python.org.
- pip: Typically comes with Python. Verify installation by running pip --version in your terminal.
- Microsoft Build Tools with C++: Required for compiling some dependencies. Download and install from Visual Studio Build Tools. During installation, ensure to check the "Desktop development with C++" workload

## Setup
1. Clone or Download the Project
   - Clone the repository using git: 
   ```bash
   git clone https://github.com/yourusername/jd-jrs-mapping-bot.git
   ```
   - Or download the project as a ZIP file from the repository and extract it.

2. Navigate to the project directory
   - Open your terminal or command prompt and navigate to the directory where you cloned or extracted the project
   ```bash
   cd path/to/jd-jrs-mapping-bot
   ```
3. Download and prepare ChromaDB
   - Download ChromaDB.zip: Ensure the file is available in the same directory as your project files. If not, download it from the specified location or repository.
   - Paste the ZIP file in the project directory if it's not already there.
   - Extract the ZIP file:
7. Extract the zip file in the same directory.
8. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
9. Run the application by opening terminal or command prompt in the same path and type:
    ```bash
    streamlit run app.py
    ```

## Usage
- Enter your query in the text area and click "Submit" to get results.

## Contributions
Contributions to the ChatBot project, particularly enhancements or optimizations for JD to JRS mapping, are encouraged. If you have suggestions for improvements or would like to contribute new features, please feel free to submit a pull request or open an issue on the repository.

## License
This ChatBot is provided under the [MIT License](LICENSE). You are free to modify and distribute the code for your own purposes.
