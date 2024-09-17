import tkinter, hashlib, random
from tkinter import messagebox, ttk


def generate_smth():
    smth = random.randint(123456, 999999)
    return str(smth)

def hashed_password_with_smth(password, smth):
    hashed_pass = hashlib.md5((smth + password).encode()).hexdigest()
    return hashed_pass

def entered_password_check(pass_input, hashed_pass, smth):
    hashed_inputed_pass = hashlib.md5((smth + pass_input).encode()).hexdigest()
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
stored_smth = generate_smth()


def register_user():
    username = register_username_entry.get()
    password = hashed_password_with_smth(register_password_entry.get(),stored_smth)


    if username and password:
        global stored_username, stored_hash
        stored_hash = hashed_password_with_smth(password, stored_smth)
        stored_username = username
        messagebox.showinfo("+", "регистрация успешна")
    else:
        messagebox.showerror("-", "не все поля заполнены")


def login_user():
    username = login_username_entry.get()
    password = hashed_password_with_smth(login_password_entry.get(),stored_smth)

    if username == stored_username and stored_hash:
        if entered_password_check(password, stored_hash, stored_smth):
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