# 📋 Task Manager

Welcome to **Task Manager** – a Python application for managing tasks with a sleek graphical interface! 🚀

## 🔧 Features

- 🔒 **User Authentication**:
  - Log in with a username and password.
  - Register new accounts with password matching validation.
  - Passwords are securely hashed using SHA-256.

- 🛠️ **Personal Dashboard**:
  - Accessible after successful login.
  - Smooth transition between login and dashboard windows.

- 🖼️ **User-Friendly Interface**:
  - Built with `CustomTkinter` for a modern look and feel.
  - Light theme support for better readability.

## 🛠️ Technologies Used

- **Programming Language**: Python 🐍
- **Libraries**:
  - [`CustomTkinter`](https://github.com/TomSchimansky/CustomTkinter) for the GUI 🖌️
  - [`SQLite`](https://www.sqlite.org/) for database management 🗄️
  - [`hashlib`](https://docs.python.org/3/library/hashlib.html) for password hashing 🔒
  - [`Pillow`](https://python-pillow.org/) for image processing 🖼️

## 🚀 How to Run

1. Ensure you have Python 3.9+ installed 🐍.
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/task-manager.git
   cd task-manager
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   python main.py

## 📂 Project Structure
```bash
Task Manager/
├── database.py          # Database management with SQLite
├── cabinet.py           # Personal dashboard functionality
├── main.py              # Main application file
├── img/                 # Folder containing icons and images
├── requirements.txt     # Required libraries
└── README.md            # Project description
```
## 🛡️ Security
- Passwords are securely stored in the database using SHA-256 hashing 🔒.
- Error handling ensures smooth operation.

## ✨ Future Enhancements
- 🔍 Add password recovery via email.
- 📝 Implement task management features.
- 📊 Include analytics and task statistics.
