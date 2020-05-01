import tkinter as tk
import requests
from AppLogic import AppLogic
from ChatPage import ChatPage


class ChatListPage(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        tk.Label(self, text="All Available Chat").pack()

        container = tk.Frame(self, width=800, height=500)

        canvas = tk.Canvas(container)
        scroll_y = tk.Scrollbar(container, orient="vertical", command=canvas.yview)

        self.rooms_frame = tk.Frame(canvas)

        # put the frame in the canvas
        canvas.create_window(0, 0, anchor='nw', window=self.rooms_frame)
        # make sure everything is displayed before configuring the scrollregion
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'),
                         yscrollcommand=scroll_y.set,
                         width=780,
                         height=500)

        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')
        
        container.pack()

        joining_frame = tk.Frame(self)
        tk.Label(joining_frame, text="Invite Code: ").grid(row=0, column=0)
        self.invite_code_entry = tk.Entry(joining_frame)
        self.invite_code_entry.grid(row=0, column=1)
        tk.Button(joining_frame, text="Join", command=self.post_join).grid(row=0, column=2)
        tk.Button(joining_frame, text="Create Room", command=self.on_create).grid(row=0, column=3)
        self.chat_page = None
        self.create_page = None
        joining_frame.pack()
        self.chat_buttons = {}

    def post_join(self):
        if self.invite_code_entry.get() != "":
            payload = {'invite_code': self.invite_code_entry.get()}
            response = requests.post(AppLogic.server_ip + "chats/join", payload, auth=AppLogic.auth)
            print(response.status_code)

    def post_leave(self):
        #TODO
        pass

    def on_create(self):
        if self.create_page is not None:
            AppLogic.root.wm_geometry("270x50")
            self.create_page.lift()

    def on_click_chat(self, button):
        AppLogic.chat_pages[self.chat_buttons[button]].lift()

    def fetch_all_chats(self):
        count = 0
        for room in AppLogic.chats:

            AppLogic.chat_pages.append(self.create_chat_page(count))

            room_frame = tk.Frame(self.rooms_frame)
            room_frame.grid_columnconfigure(0, weight=1)  # help me config the weight
            room_frame.grid_rowconfigure(0, weight=1)
            tk.Label(room_frame, text=room['name']).grid(row=0, column=0)
            tk.Label(room_frame, text="Invite Code: " + room['invite_code']).grid(row=1, column=0)
            self.chat_buttons[self.create_button(room_frame)] = count
            tk.Button(room_frame, text="Leave").grid(row=1, column=1)
            room_frame.pack(side="top", fill="both", expand=False)
            count = count + 1

    def create_chat_page(self, index):
        chat_page = ChatPage(AppLogic.container)
        chat_page.index = index
        chat_page.place(in_=AppLogic.container, x=0, y=0, relwidth=1, relheight=1)
        chat_page.back_redirect = self
        chat_page.fetch_message()
        return chat_page

    def create_button(self, room_frame):
        button = tk.Button(room_frame, text="Chat")
        button.configure(command=lambda: self.on_click_chat(button))
        button.grid(row=0, column=1)
        return button

