# utils.py
def load_user(username):
    fake_db = {"admin": "admin123", "user": "pass"}
    return fake_db.get(username)