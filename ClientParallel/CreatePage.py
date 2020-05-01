import tkinter as tk
import requests
from AppLogic import AppLogic, HTTPBearerAuth
import requests

class CreatePage(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        tk.Label(self, text="Name: ").grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)
        tk.Button(self, text="Create", command=self.on_create).grid(row=0, column=2)
        tk.Button(self, text="Back", command=self.redirect).grid(row=0, column=3)
        self.redirect_page = None

    def redirect(self):
        if self.redirect_page is not None:
            self.redirect_page.fetch_all_chats()
            AppLogic.root.wm_geometry("800x600")
            self.redirect_page.lift()

    def on_create(self):
        if self.name_entry.get() != "":
            payload = {'name': self.name_entry.get()}
            response = requests.post(AppLogic.server_ip+"chats", payload, auth=AppLogic.auth)
            if response.status_code == 201:
                self.redirect()
