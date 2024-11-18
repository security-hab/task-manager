import random
import tkinter

import customtkinter as ctk
from PIL import Image

from citations import citate


def loadImage(path):  # Добавлено: новая функция для обработки изображений
    img = Image.open(path).convert("RGBA")
    data = img.getdata()
    new_data = [(255, 255, 255, item[3]) for item in data]
    img.putdata(new_data)
    return img


imgHomeBtn = ctk.CTkImage(
    dark_image=loadImage(r"img\home.ico"), size=(12, 12)
)
imgTasksInBtn = ctk.CTkImage(
    dark_image=loadImage(r"img\main.ico"), size=(12, 12)
)
imgExitBtn = ctk.CTkImage(
    dark_image=loadImage(r"img\login.ico"), size=(12, 12)
)
imgTelegramBtn = ctk.CTkImage(
    dark_image=loadImage(r"img\telegram.ico"), size=(12, 12)
)
imgSettingsBtn = ctk.CTkImage(
    dark_image=loadImage(r"img\settings.ico"), size=(12, 12)
)
imgAboutBtn = ctk.CTkImage(
    dark_image=loadImage(r"img\about.ico"), size=(12, 12)
)


def personalCabinet(app):
    cabinetWindow = ctk.CTkToplevel()
    cabinetWindow.title("Task Manager")
    cabinetWindow.geometry("600x400+700+200")
    cabinetWindow.minsize(600, 400)
    # cabinetWindow.resizable(False, False)
    cabinetWindow.configure(fg_color="white")
    cabinetWindow.after(
        200,
        lambda: cabinetWindow.iconbitmap(r"img\logo.ico"),
    )

    # cabinetWindow.after(0, lambda: cabinetWindow.state("zoomed"))
    cabinetWindow.after(100, lambda: cabinetWindow.focus_force())
    cabinetWindow.grid_rowconfigure(0, weight=1)
    cabinetWindow.grid_columnconfigure(1, weight=1)

    btnWidth = 100
    btnHeight = 10

    checkboxVar = ctk.IntVar()

    navPanel = ctk.CTkFrame(
        cabinetWindow, width=180, fg_color="#ff5722", corner_radius=0
    )
    navPanel.grid(row=0, column=0, sticky="ns", pady=(0, 0), padx=(0, 0))

    contentFrame = ctk.CTkFrame(cabinetWindow, fg_color="white")
    contentFrame.grid(row=0, column=1, sticky="nsew", padx=(0, 0), pady=(0, 0))

    def updateContent(content):
        for widget in contentFrame.winfo_children():
            widget.destroy()

        contentLabel = ctk.CTkLabel(
            contentFrame, text=content, font=("JetBrains Mono", 16)
        )
        contentLabel.pack(pady=20)

    def homePage():
        for widget in contentFrame.winfo_children():
            widget.destroy()

        welcomeLabel = ctk.CTkLabel(
            contentFrame,
            text="Welcome to Task Manager!",
            font=("JetBrains Mono", 18, "bold"),
        )
        welcomeLabel.pack(pady=(10, 0))

        citateLabel = ctk.CTkLabel(
            contentFrame,
            text=random.choice(citate),
            font=("JetBrains Mono", 10),
            fg_color="black",
            height=12,
            text_color="white",
        )
        citateLabel.pack(pady=(0, 0), padx=(0, 0), anchor="s", side="top", fill="x")

    homePage()

    def taskBtnAction():
        for widget in contentFrame.winfo_children():
            widget.destroy()

        contentFrame.grid_rowconfigure(0, weight=1)
        contentFrame.grid_rowconfigure(1, weight=0)

        # Создание текстового поля
        taskLabelFrame = ctk.CTkEntry(
            contentFrame,
            placeholder_text="Your task",
            corner_radius=2,
            border_color="#ff5722",
            border_width=1,
            font=("Robot", 12),
        )
        taskLabelFrame.grid(column=0, row=1, pady=(0, 2), padx=(2, 0), sticky="we")

        taskList = ctk.CTkScrollableFrame(contentFrame, fg_color="white")
        taskList.grid(column=0, row=0, columnspan=2, sticky="nsew")
        contentFrame.grid_columnconfigure(0, weight=1)

        def addTask(event=None):
            taskText = taskLabelFrame.get()
            if taskText:
                taskCheckbox = ctk.CTkCheckBox(
                    taskList,
                    text=taskText,
                    font=("Roboto", 12),
                    fg_color="#ff5722",
                    corner_radius=3,
                )

                taskCheckbox.pack(fill="x", padx=5, pady=2)
                taskLabelFrame.delete(0, "end")

        taskLabelFrame.bind("<Return>", addTask)

        # Создание кнопки
        taskBtnFrame = ctk.CTkButton(
            contentFrame,
            text="Add",
            width=80,
            fg_color="#ff5722",
            font=("Roboto", 12, "bold"),
            corner_radius=3,
            hover_color="#ff764d",
            command=addTask,
        )
        taskBtnFrame.grid(column=1, row=1, pady=(0, 2), padx=(2, 2), sticky="e")

        contentFrame.grid_columnconfigure(0, weight=1)
        contentFrame.grid_columnconfigure(1, weight=0)

    def logout():
        cabinetWindow.destroy()
        app.deiconify()

    homeBtn = ctk.CTkButton(
        navPanel,
        text="Home",
        command=lambda: homePage(),
        fg_color="transparent",
        text_color="white",
        hover_color="#ff764d",
        font=("Roboto", 12, "bold"),
        cursor="hand2",
        width=btnWidth,
        height=btnHeight,
        anchor="w",
        image=imgHomeBtn,
        compound="left",
        corner_radius=0,
    )
    homeBtn.grid(row=0, column=0, padx=(1, 1), pady=(5, 5), sticky="we")

    taskBtn = ctk.CTkButton(
        navPanel,
        text="Tasks",
        command=lambda: taskBtnAction(),
        fg_color="transparent",
        text_color="white",
        hover_color="#ff764d",
        font=("Roboto", 12, "bold"),
        cursor="hand2",
        width=btnWidth,
        height=btnHeight,
        anchor="w",
        image=imgTasksInBtn,
        compound="left",
        corner_radius=0,
    )
    taskBtn.grid(row=1, column=0, padx=(1, 1), pady=(5, 5), sticky="we")

    exitBtn = ctk.CTkButton(
        navPanel,
        text="Exit",
        command=lambda: logout(),
        fg_color="transparent",
        text_color="white",
        hover_color="#ff764d",
        font=("Roboto", 12, "bold"),
        cursor="hand2",
        width=btnWidth,
        height=btnHeight,
        anchor="w",
        image=imgExitBtn,
        compound="left",
        corner_radius=0,
    )
    exitBtn.grid(row=5, column=0, padx=(1, 1), pady=(5, 5), sticky="we")
