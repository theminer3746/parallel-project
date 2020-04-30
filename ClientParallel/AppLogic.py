import tkinter as tk


class AppLogic:

    username = ""
    chats = {('0', 'Test01'): 'Test01', ('1', 'Test02'): 'Test02'}
    server_ip = ""
    root = tk.Tk()
    token = ""
    append_file = None
    current_room = None
    current_chats = None


