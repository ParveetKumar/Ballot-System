import bcrypt

class Auth:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.cursor = db_conn.cursor()

    def register_user(self, username, password, name):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.cursor.execute(
            "INSERT INTO users (username, password, name) VALUES (%s, %s, %s)",
            (username, hashed_password, name)
        )
        self.db_conn.commit()

    def login_user(self, username, password):
        self.cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        result = self.cursor.fetchone()
        if result and bcrypt.checkpw(password.encode(), result[0].encode()):
            print("Login successful")
            return True
        print("Login failed")
        return False
