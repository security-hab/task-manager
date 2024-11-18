# 🌟 Wallpaper Changer 🖼️

This project is a Python-based application that changes the desktop wallpaper randomly from a specified folder. It includes a tray icon that provides easy access to change the wallpaper or exit the application.

## ✨ Features
- **🎲 Random Wallpaper Selection**: Selects and sets a random image from the specified folder.
- **⌨️ Hotkey Support**: Change the wallpaper using a predefined hotkey (`Win + Alt`).
- **🖱️ Tray Icon Menu**: A system tray icon with a menu for easy control.
- **🔄 Automatic Wallpaper Update**: Periodically checks for new images in the folder.

## 🛠️ Requirements
- Python 3.x
- `Pillow` for image handling
- `pystray` for creating the system tray icon
- `keyboard` for hotkey detection

## 🚀 Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/security-hab/wallpaper-changer.git
    cd wallpaper-changer
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Ensure that the `config.py` file is configured with the path to your wallpaper folder:
    ```python
    # config.py
    WallpaperFolderPath = r"C:\path\to\your\wallpapers"
    ```

## 📋 Usage
1. Run the main script:
    ```bash
    python main.py
    ```
2. The application will run in the background and display an icon in the system tray.
3. Use the `Win + Alt` hotkey to change the wallpaper.
4. Right-click the tray icon to access options like "Change Wallpaper" or "Exit".

## 🗂️ Project Structure
```
wallpaperChanger/
│
├── assets/
│   └── icon.jpg
│
├── main.py
├── config.py
├── README.md
└── requirements.txt
```

## ⚠️ Notes
- Ensure that the `icon.jpg` file is included in the `assets` folder for the tray icon to work.
- The program supports common image formats such as `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.gif`.

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 🙏 Acknowledgements
- [Pillow](https://python-pillow.org/) 🖼️
- [pystray](https://github.com/moses-palmer/pystray) 🖥️
- [keyboard](https://github.com/boppreh/keyboard) ⌨️

Enjoy your personalized wallpaper experience! 🎉

