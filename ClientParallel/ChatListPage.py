import tkinter as tk
import requests
from AppLogic import AppLogic

class ChatListPage(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        tk.Label(self, text="All Available Chat").pack()
        
        rooms_frame = tk.Frame(self)
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
        rooms_frame.pack(side="top", fill="both", expand=False)

        joining_frame = tk.Frame(self)
        tk.Label(joining_frame, text="id: ").grid(row=0, column=0)
        self.id_join_entry = tk.Entry(joining_frame)
        self.id_join_entry.grid(row=0, column=1)
        tk.Button(joining_frame, text="Join").grid(row=0, column=2)
        self.chat_page = None
        joining_frame.pack()

    def post_update(self):
        # TODO
        pass

    def post_leave(self):
        #TODO
        pass

    def on_click_chat(self, room):
        AppLogic.current_room = room
        AppLogic.current_chats = AppLogic.chats[room]
        self.chat_page.lift()
