# 📁 File Organizer (Python Automation Tool)

## 🚀 Overview

File Organizer is a Python-based command-line tool that automatically organizes files in a directory into categorized folders based on file types.

It is designed to simplify file management by reducing manual effort and ensuring a clean, structured directory.


## ✨ Features

* 📂 Automatic file categorization (Documents, Images, Videos, etc.)
* 🔁 Duplicate file handling (auto-renaming with suffix)
* 🧾 Logging system (file + console logging)
* 🧪 Dry-run mode (simulate actions without making changes)
* ⚙️ Config-driven design (easy to customize categories)
* 📊 Summary report (files processed and moved)
* 🖥️ CLI-based execution


## 🛠️ Tech Stack

* Python 3
* Standard libraries:

  * os
  * shutil
  * argparse
  * logging


## 📁 Project Structure

file-organizer/
│
├── organizer.py        # Main script
├── config.py           # File type mappings & settings
├── logger.py           # Logging configuration
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── logs/
    └── organizer.log   # Log file


## ⚙️ Installation

1. Clone the repository:

git clone https://github.com/yourusername/file-organizer.git
cd file-organizer

2. (Optional) Create virtual environment:

python -m venv venv
venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt


## ▶️ Usage

### 🔹 Basic Run

python organizer.py --path "C:\Users\YourName\Downloads"

If no path is provided, the script defaults to the **Downloads folder**.


### 🔹 Dry Run Mode (Recommended)

python organizer.py --path "C:\Users\YourName\Downloads" --dry-run

👉 Simulates file movement without making any changes.


## 📊 Example Output

INFO - Moved: file1.pdf → Docs
INFO - Moved: image1.jpg → Images
INFO - Processed: 10, Moved: 8


## 🧠 How It Works

1. Reads all files in the target directory
2. Matches file extensions with predefined categories
3. Creates folders if they don’t exist
4. Handles duplicate filenames safely
5. Moves files into appropriate folders
6. Logs all operations for traceability


## ⚙️ Configuration

You can modify file categories in `config.py`:

FILE_TYPES = {
    "Docs": [".txt", ".pdf", ".docx"],
    "Images": [".jpg", ".png"],
    ...
}


## 🔮 Future Enhancements

* GUI-based interface
* Scheduled automation
* Recursive directory support
* Cloud storage integration
* File preview before moving


## 💼 Resume Highlight

> Developed a Python-based file automation tool with CLI support to organize directories, featuring logging, duplicate handling, and configurable file categorization.


## 📜 License

This project is open-source and available under the MIT License.


## 🙌 Acknowledgements

Built as part of a hands-on Python portfolio to demonstrate real-world automation and backend development skills.
