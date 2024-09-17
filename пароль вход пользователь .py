import tkinter, hashlib, random
from tkinter import messagebox, ttk


def generate_salt():
    salt = random.randint(123456, 999999)
    return str(salt)

def hashed_password_with_salt(password, salt):
    hashed_pass = hashlib.md5((salt + password).encode()).hexdigest()
    return hashed_pass

def entered_password_check(pass_input, hashed_pass, salt):
    hashed_inputed_pass = hashlib.md5((salt + pass_input).encode()).hexdigest()
    return hashed_inputed_pass == hashed_pass



root = tkinter.Tk()
root.title("окно регистрации")

notebook = ttk.Notebook(root)
register_tab = tkinter.Frame(notebook)
login_tab = tkinter.Frame(notebook)
notebook.add(register_tab, text="регистрация")
notebook.add(login_tab, text="вход")
notebook.pack(fill="both")
stored_username = ""
stored_hash = ""
stored_salt = ""


def register_user():
    username = register_username_entry.get()
    password = register_password_entry.get()

    if username and password:
        global stored_username, stored_hash, stored_salt
        stored_salt = generate_salt()
        stored_hash = hashed_password_with_salt(password, stored_salt)
        stored_username = username
        messagebox.showinfo("+", "регистрация успешна")
    else:
        messagebox.showerror("-", "не все поля заполнены")


def login_user():
    username = login_username_entry.get()
    password = login_password_entry.get()

    if username == stored_username and stored_hash:
        if entered_password_check(password, stored_hash, stored_salt):
            messagebox.showinfo("+", "успешный вход")
        else:
            messagebox.showerror("-", "неправильный пароль")
    else:
        messagebox.showerror("-", "несуществующий пользователь")


tkinter.Label(register_tab, text="логин:").pack(pady=5)
register_username_entry = tkinter.Entry(register_tab)
register_username_entry.pack(pady=5)
tkinter.Label(register_tab, text="пароль:").pack(pady=5)
register_password_entry = tkinter.Entry(register_tab, show="*")
register_password_entry.pack(pady=5)
tkinter.Button(register_tab, text="регистрация", command=register_user).pack(pady=10)
tkinter.Label(login_tab, text="логин:").pack(pady=5)
login_username_entry = tkinter.Entry(login_tab)
login_username_entry.pack(pady=5)
tkinter.Label(login_tab, text="пароль:").pack(pady=5)
login_password_entry = tkinter.Entry(login_tab, show="*")
login_password_entry.pack(pady=5)
tkinter.Button(login_tab, text="войти", command=login_user).pack(pady=10)
root.mainloop()