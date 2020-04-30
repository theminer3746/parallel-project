import tkinter as tk
from UserPage import UserPage
from ChatListPage import ChatListPage
from ChatPage import ChatPage
from AppLogic import AppLogic

if __name__ == '__main__':
    container = tk.Frame(AppLogic.root)
    container.pack(side="top", fill="both", expand=True)
    # initialize all page
    user_page = UserPage(container)
    chat_list_page = ChatListPage(container)
    chat_page = ChatPage(container)
    user_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    chat_list_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    chat_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

    # set path
    user_page.next_page = chat_list_page
    chat_list_page.chat_page = chat_page
    chat_page.back_redirect = chat_list_page

    # set user_page as first page
    user_page.lift()
    AppLogic.root.mainloop()

if __name__ == '__test__':
    root = tk.Tk()
    container = tk.Frame(root)
    container.pack(side="top", fill="both", expand=True)

    chat_page = ChatPage(container)
    chat_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

    chat_page.lift()

    root.wm_geometry("800x600")
    root.mainloop()