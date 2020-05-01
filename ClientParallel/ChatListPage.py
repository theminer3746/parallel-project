import tkinter as tk
import requests
from AppLogic import AppLogic


class ChatListPage(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        tk.Label(self, text="All Available Chat").pack()

        container = tk.Frame(self, width=800, height=500)

        canvas = tk.Canvas(container)
        scroll_y = tk.Scrollbar(container, orient="vertical", command=canvas.yview)

        rooms_frame = tk.Frame(canvas)
        count = 0

        for room in AppLogic.chats.keys():
            room_frame = tk.Frame(rooms_frame)
            room_frame.grid_columnconfigure(0, weight=1) # help me config the weight
            room_frame.grid_rowconfigure(0, weight=1)
            tk.Label(room_frame, text=room[1]).grid(row=0, column=0)
            tk.Label(room_frame, text="ID: "+room[0]).grid(row=1, column=0)
            tk.Button(room_frame, text="Chat", command=lambda: self.on_click_chat(room)).grid(row=0, column=1)
            tk.Button(room_frame, text="Leave").grid(row=1, column=1)
            room_frame.pack(side="top", fill="both", expand=False)
            count = count + 1
        # put the frame in the canvas
        canvas.create_window(0, 0, anchor='nw', window=rooms_frame)
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

    def on_click_chat(self, room):
        AppLogic.current_room = room
        AppLogic.current_chats = AppLogic.chats[room]
        self.chat_page.lift()
