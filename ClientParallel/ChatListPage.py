import tkinter as tk
import requests
from AppLogic import AppLogic

class ChatListPage(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        tk.Label(self, text="All Available Chat").pack()
        for room in AppLogic.chats.keys():
            room_frame = tk.Frame(self)
            room_frame.grid_columnconfigure(0, weight=1) # help me config the weight
            room_frame.grid_rowconfigure(0, weight=1)
            tk.Label(room_frame, text=room[1]).grid(row=0, column=0)
            tk.Label(room_frame, text="ID: "+room[0]).grid(row=1, column=0)
            tk.Button(room_frame, text="Chat").grid(row=0, column=1)
            tk.Button(room_frame, text="Leave").grid(row=1, column=1)
            room_frame.pack(side="top", fill="both", expand=False)


    def post_update(self):
        # TODO
        pass