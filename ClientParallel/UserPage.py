import tkinter as tk
from AppLogic import AppLogic
import requests


class UserPage(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        AppLogic.root.wm_geometry("200x70")
        self.username_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self, show="*")
        submit_button = tk.Button(self, text="submit", command=self._on_submit)
        tk.Label(self, text="username: ").grid(row=0, sticky=tk.W)
        self.username_entry.grid(row=0, column=1)
        tk.Label(self, text="password: ").grid(row=1, sticky=tk.W)
        self.password_entry.grid(row=1, column=1)
        submit_button.grid(row=2, columnspan=2)
        self.next_page = None
        self.user = None
        register_button = tk.Button(self, text="register", command=self._on_register)
        register_button.grid(row=2, columnspan=1)

    def _on_submit(self):
          # set new display size
        self.post_login()

    def _on_register(self):
        print("Register complete")
        self.post_register()
        self._on_submit()

    def get_username(self):
        return self.username_entry.get()

    def post_login(self):
        login_payload = {'username': self.username_entry.get(), "password": self.password_entry.get()}
        response = requests.post(AppLogic.server_ip+'auth/login', data=login_payload)
        if response.status_code == 200:
            res = response.json()
            AppLogic.token = res['access_token']
            AppLogic.setup_auth()
            AppLogic.root.wm_geometry("800x600")
            self.get_chats()
            self.next_page.lift()

    def get_chats(self):
        response = requests.get(AppLogic.server_ip+'chats', auth=AppLogic.auth)
        if response.status_code == 200:
            AppLogic.chats = response.json()[0]
            self.next_page.fetch_all_chats()
            
    def post_register(self):
        register_payload = {'username': self.username_entry.get(), "password": self.password_entry.get()}
        response = requests.post(AppLogic.server_ip+'users', data=register_payload)
        if response.status_code == 201:
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')

            

