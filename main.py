from db.db_connection import connect_db
from app.auth import Auth
from app.lottery import Lottery
from app.repayment import RepaymentPlan
from app.models import Person

def main():
    conn = connect_db()
    auth = Auth(conn)
    lottery = Lottery(conn)
    repayment = RepaymentPlan(conn)

    print("1. Register\n2. Login")
    choice = input("Choose an option: ")

    if choice == '1':
        username = input("Username: ")
        password = input("Password: ")
        name = input("Name: ")
        auth.register_user(username, password, name)
    elif choice == '2':
        username = input("Username: ")
        password = input("Password: ")
        if auth.login_user(username, password):
            print("Logged in successfully!")

    conn.close()

if __name__ == "__main__":
    main()
