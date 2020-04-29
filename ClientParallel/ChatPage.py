import tkinter as tk
from AppLogic import AppLogic
import threading
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

class ChatPage(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        tk.Label(self, text="Chat Test").pack()
        message_frame = tk.Frame(self)
        scrollbar = tk.Scrollbar(message_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.mylist = tk.Listbox(message_frame, yscrollcommand=scrollbar.set, width=800, height=30)

        self.mylist.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=self.mylist.yview)
        message_frame.pack(side="top", fill="both", expand=False)

        tail = tk.Frame(self, width=800)
        self.message_entry = tk.Entry(tail)
        self.message_entry.grid(row=0, column=0)
        tk.Button(tail, text="Send", command=self.send).grid(row=0, column=1)
        tail.pack(side="top", fill="both", expand=False)

        # initialize socket connection
        self.connection = None
        self.socket_thread = threading.Thread(target=self.client_socket)
        self.socket_thread.start()
        self.chats = []

    def send(self):
        self.connection.sendall(self.message_entry.get().encode())

    def client_socket(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.connection:
            self.connection.connect((HOST, PORT))
            while True:
                data = self.connection.recv(1024)
                self.mylist.insert(tk.END, repr(data))

