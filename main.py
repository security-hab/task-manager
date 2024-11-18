import hashlib
import sqlite3
from tkinter import messagebox

import customtkinter as ctk
from PIL import Image

import database
from cabinet import personalCabinet

app = ctk.CTk(fg_color="white")
app.geometry("300x500+700+200")
app.title("Task Manager")
app.resizable(False, False)
ctk.set_appearance_mode("light")  # Светлая тема для белого фона
app.iconbitmap(r"img\main.ico")

# Настройка колонок и строк
app.grid_columnconfigure(0, weight=1)


for i in range(7):
    app.grid_rowconfigure(i, weight=1)

conn = database.connectDB()
database.createTables(conn)
cursor = conn.cursor()


def loadImage(path):  # Добавлено: новая функция для обработки изображений
    img = Image.open(path).convert("RGBA")
    data = img.getdata()
    new_data = [(255, 255, 255, item[3]) for item in data]
    img.putdata(new_data)
    return img


imgSignUpBtn = ctk.CTkImage(
    dark_image=loadImage(r"img\add.ico"), size=(12, 12)
)
imgSignInBtn = ctk.CTkImage(
    dark_image=loadImage(r"img\login.ico"), size=(12, 12)
)
imgGoogleBtn = ctk.CTkImage(
    dark_image=loadImage(r"img\google.ico"), size=(12, 12)
)


def hashingPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()


def userRegistration(
    username,
    email,
    password,
    password_confirmation,
    userEntry,
    userMail,
    userPassword,
    userConfirmPassword,
):
    if password != password_confirmation:
        messagebox.showerror("Error", "Passwords do not match!")
        signWindow.focus_force()
        return False
    hashedPassword = hashingPassword(password)
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hashedPassword),
        )
        conn.commit()
        messagebox.showinfo("Success", "Username was successfully registrated!")

        userEntry.delete(0, ctk.END)
        userMail.delete(0, ctk.END)
        userPassword.delete(0, ctk.END)
        userConfirmPassword.delete(0, ctk.END)

        destroySignWindow()

        return True
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username or Email already exist!")
        signWindow.focus_force()
        return False


def userLogin(username, password, loginEntry, passwordEntry):
    hashed_password = hashingPassword(password)
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, hashed_password),
    )

    result = cursor.fetchone()
    if result:
        # messagebox.showinfo("Success", f"Welcome back {username}")
        loginEntry.delete(0, ctk.END)
        passwordEntry.delete(0, ctk.END)

        if "signWindow" in globals():
            destroySignWindow()

        app.withdraw()

        personalCabinet(app)
        # app.destroy()
    else:
        messagebox.showerror("Error", "Invalid username or password")


def destroySignWindow():
    signWindow.destroy()
    app.focus_force()


def signUpWindow():
    global signWindow
    signWindow = ctk.CTkToplevel(app)
    signWindow.title("Sign Up")
    signWindow.geometry("300x500+700+200")
    signWindow.resizable(False, False)
    signWindow.configure(fg_color="white")
    signWindow.after(100, lambda: signWindow.focus_force())

    signWindow.grid_columnconfigure(0, weight=1)

    for i in range(10):
        signWindow.grid_rowconfigure(i, weight=1)

    regLabel = ctk.CTkLabel(
        signWindow,
        text="Sign Up",
        font=("JetBrains Mono", 25, "bold"),
        text_color="black",
    )
    regLabel.grid(column=0, row=0, pady=(40, 5), sticky="n")

    createAccountLabel = ctk.CTkLabel(
        signWindow,
        text="Create your account",
        font=("JetBrains Mono", 12),
        text_color="gray",
    )
    createAccountLabel.grid(column=0, row=1, pady=(0, 5), sticky="n")

    additionalChoise = ctk.CTkLabel(
        signWindow, text="or", font=("JetBrains Mono", 12), text_color="black"
    )
    additionalChoise.grid(column=0, row=7, pady=(0, 0), sticky="n")

    userEntry = ctk.CTkEntry(
        signWindow,
        placeholder_text="Username",
        height=40,
        width=220,
        fg_color="#f9eceb",
        corner_radius=10,
    )
    userEntry.grid(column=0, row=2, padx=20, pady=(0, 0), sticky="n")

    userMail = ctk.CTkEntry(
        signWindow,
        placeholder_text="Mail",
        height=40,
        width=220,
        fg_color="#f9eceb",
        corner_radius=10,
    )
    userMail.grid(column=0, row=3, padx=20, pady=(0, 0), sticky="n")

    userPassword = ctk.CTkEntry(
        signWindow,
        placeholder_text="Password",
        show="*",
        height=40,
        width=220,
        fg_color="#f9eceb",
        corner_radius=10,
    )
    userPassword.grid(column=0, row=4, padx=20, pady=(0, 0), sticky="n")

    userConfirmPassword = ctk.CTkEntry(
        signWindow,
        placeholder_text="Confirm password",
        show="*",
        height=40,
        width=220,
        fg_color="#f9eceb",
        corner_radius=10,
    )
    userConfirmPassword.grid(column=0, row=5, padx=20, pady=(0, 0), sticky="n")

    singUpButton = ctk.CTkButton(
        signWindow,
        text="Sign Up",
        fg_color="#ff5722",
        height=40,
        width=220,
        corner_radius=10,
        text_color="white",
        cursor="hand2",
        image=imgSignUpBtn,
        compound="left",
        command=lambda: userRegistration(
            userEntry.get(),
            userMail.get(),
            userPassword.get(),
            userConfirmPassword.get(),
            userEntry,
            userMail,
            userPassword,
            userConfirmPassword,
        ),
    )
    singUpButton.grid(column=0, row=6, pady=(0, 0))

    singUpGoogle = ctk.CTkButton(
        signWindow,
        text="Log in with Google",
        fg_color="#ff5722",
        text_color="white",
        corner_radius=10,
        cursor="hand2",
        width=220,
        height=40,
        image=imgGoogleBtn,
        compound="left",
    )
    singUpGoogle.grid(column=0, row=8, pady=(0, 0), sticky="n")

    loginAccount = ctk.CTkButton(
        signWindow,
        text="Already have an account? Login",
        font=("JetBrains Mono", 10),
        text_color="#ff5722",
        cursor="hand2",
        fg_color="transparent",
        hover_color="white",
        command=destroySignWindow,
    )
    loginAccount.grid(column=0, row=9, pady=(0, 0), sticky="n")


# Заголовок
introLabel = ctk.CTkLabel(
    app, text="Welcome Back", font=("JetBrains Mono", 25, "bold"), text_color="black"
)
introLabel.grid(column=0, row=0, pady=(40, 5), sticky="n")

# Описание под заголовком
descriptionLabel = ctk.CTkLabel(
    app,
    text="Enter your credential for login",
    font=("JetBrains Mono", 12),
    text_color="gray",
)
descriptionLabel.grid(column=0, row=1, pady=(0, 20), sticky="n")

# Поле для логина
loginEntry = ctk.CTkEntry(
    app,
    placeholder_text="Username",
    height=40,
    width=220,
    fg_color="#f9eceb",
    corner_radius=10,
)
loginEntry.grid(column=0, row=2, padx=20, pady=5)

# Поле для пароля
passwordEntry = ctk.CTkEntry(
    app,
    placeholder_text="Password",
    height=40,
    width=220,
    fg_color="#f9eceb",
    corner_radius=10,
    show="*",
)
passwordEntry.grid(column=0, row=3, padx=20, pady=5)

# Кнопка входа
loginButton = ctk.CTkButton(
    app,
    text="Login Now",
    height=40,
    width=220,
    fg_color="#ff5722",
    corner_radius=10,
    text_color="white",
    cursor="hand2",
    image=imgSignInBtn,
    compound="left",
    command=lambda: userLogin(
        loginEntry.get(), passwordEntry.get(), loginEntry, passwordEntry
    ),
)
loginButton.grid(column=0, row=4, pady=20)
app.bind(
    "<Return>",
    lambda event: userLogin(
        loginEntry.get(), passwordEntry.get(), loginEntry, passwordEntry
    ),
)

# Ссылка на восстановление пароля
forgotPasswordLabel = ctk.CTkLabel(
    app,
    text="Forgot password?",
    font=("JetBrains Mono", 10),
    text_color="#ff5722",
    cursor="hand2",
)
forgotPasswordLabel.grid(column=0, row=5, pady=(5, 20))

# Ссылка на регистрацию
signUpLabel = ctk.CTkButton(
    app,
    text="Don't have an account? Sign Up",
    font=("JetBrains Mono", 10),
    text_color="#ff5722",
    cursor="hand2",
    fg_color="transparent",
    hover_color="white",
    command=signUpWindow,
)
signUpLabel.grid(column=0, row=6, pady=(10, 0))

app.mainloop()
database.closeDB(conn)
