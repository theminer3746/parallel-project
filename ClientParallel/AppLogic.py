import tkinter as tk
import requests


class AppLogic:

    username = ""
    chats = {('0', 'Test01'): 'Test01', ('1', 'Test02'): 'Test02'}
    server_ip = "http://127.0.0.1:8000/api/"
    run = True
    root = tk.Tk()
    root.title("Mini-Project")
    container = None
    rooms_frame = None
    token = ""
    auth = None
    append_file = None
    current_room = None
    current_chats = None
    chat_pages = []

    @staticmethod
    def setup_auth():
        AppLogic.auth = HTTPBearerAuth(AppLogic.token)



class HTTPBearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __eq__(self, other):
        return self.token == getattr(other, 'token', None)

    def __ne__(self, other):
        return not self == other

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer ' + self.token
        return r

