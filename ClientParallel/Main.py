import tkinter as tk
from UserPage import UserPage
from ChatListPage import ChatListPage
from ChatPage import ChatPage
from AppLogic import AppLogic
from CreatePage import CreatePage

if __name__ == '__main__':
    AppLogic.container = tk.Frame(AppLogic.root)
    AppLogic.container.pack(side="top", fill="both", expand=True)
    # initialize all page
    user_page = UserPage(AppLogic.container)
    chat_list_page = ChatListPage(AppLogic.container)
    create_page = CreatePage(AppLogic.container)
    user_page.place(in_=AppLogic.container, x=0, y=0, relwidth=1, relheight=1)
    chat_list_page.place(in_=AppLogic.container, x=0, y=0, relwidth=1, relheight=1)
    create_page.place(in_=AppLogic.container, x=0, y=0, relwidth=1, relheight=1)

    # set path
    user_page.next_page = chat_list_page
    chat_list_page.create_page = create_page
    create_page.redirect_page = chat_list_page

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