import tkinter as tk
from AppLogic import AppLogic
import threading
import requests

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

class ChatPage(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        tk.Label(self, text="Test").pack()
        message_frame = tk.Frame(self)
        scrollbar = tk.Scrollbar(message_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.mlist = tk.Listbox(message_frame, yscrollcommand=scrollbar.set, width=800, height=30)

        self.mlist.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=self.mlist.yview)
        message_frame.pack(side="top", fill="both", expand=False)

        tail = tk.Frame(self, width=800)
        self.message_entry = tk.Entry(tail)
        self.message_entry.grid(row=0, column=0)
        tk.Button(tail, text="Send", command=self.send).grid(row=0, column=1)
        tk.Button(tail, text="Back", command=self.on_click_back).grid(row=1, column=0)
        tail.pack(side="top", fill="both", expand=False)

        # initialize socket connection
        self.connection = None
        # self.socket_thread = threading.Thread(target=self.client_socket)
        # self.socket_thread.start()
        self.chats = []
        self.back_redirect = None

        self.index = 0
        self.since = None

    def send(self):
        payload = {'message': self.message_entry.get()}
        print(payload)
        response = requests.post(AppLogic.server_ip + 'chats/' + AppLogic.chats[self.index]['_id'] + '/messages',
                                 payload,
                                 auth=AppLogic.auth)
        print(response.status_code)
        if response.status_code == 201:
            self.fetch_message()



    def client_socket(self):
        pass

    def on_click_back(self):
        if self.back_redirect is not None:
            self.back_redirect.lift()

    def fetch_message(self):
        if self.since is None:
            payload = {'since': ''}
        else:
            payload = {'since': self.since}

        response = requests.get(AppLogic.server_ip+'chats/'+AppLogic.chats[self.index]['_id']+'/messages', data=payload, auth=AppLogic.auth)
        if response.status_code == 200:
            messages = response.json()['messages']
            if len(messages) > 0:
                self.since = messages[-1]['created_at']
            for m in messages:
                self.mlist.insert(tk.END, m['username']+'('+m['created_at']+'): '+m['message'])

