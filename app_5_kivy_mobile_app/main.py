from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob, random
from datetime import datetime
from pathlib import Path

Builder.load_file('design.kv')

# --------------------- Utils ---------------------
def _navigate(manager, screen_name, direction='left'):
    manager.transition.direction = direction
    manager.current = screen_name

def _get_users():
    with open("users.json") as file:
        users = json.load(file)
    return users

def _write_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

# --------------------- Screens ---------------------
# * Name of these "Screen" classes MUST be same name as in design.kv
class LoginScreen(Screen):
    def sign_up(self):
        _navigate(self.manager, 'sign_up_screen')
        
    def login(self, username, password):
        users = _get_users()
        if username in users and users[username]['password'] == password:
            self.manager.current = 'login_success_screen'
        else:
            self.ids.login_wrong.text = "Wrong username or password"

class SignUpScreen(Screen):
    def add_user(self, username, password):
        users = _get_users()
        users[username] = {
            "username": username,
            "password": password,
            "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        }
        _write_users(users)
        _navigate(self.manager, 'sign_up_success_screen')

class SignUpSuccessScreen(Screen):
    def go_to_login(self):
        _navigate(self.manager, 'login_screen', direction='right')

class LoginSuccessScreen(Screen):
    def _display_quote(self, text):
        self.ids.quote.text = text

    def logout(self):
        _navigate(self.manager, 'login_screen', direction='right')

    def get_quote(self, feeling):
        feeling = feeling.lower()
        available_feelings = glob.glob("quotes/*.txt")
        
        available_feelings = [Path(filename).stem for filename in available_feelings]
        
        if feeling in available_feelings:
            with open(f"quotes/{feeling}.txt") as file:
                quotes = file.readlines()
            # Pick a line randomly
            self._display_quote(random.choice(quotes))
        else:
            self._display_quote("Try another feeling")

# --------------------- Root ---------------------
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

# --------------------- Execution ---------------------
if __name__ == '__main__':
    MainApp().run()