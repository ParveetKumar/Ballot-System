import random
from app.models import Person

class Lottery:
    def __init__(self, db_conn):
        self.participants = []
        self.db_conn = db_conn
        self.cursor = db_conn.cursor()

    def add_person(self, person, user_id):
        self.participants.append(person)
        self.cursor.execute(
            "INSERT INTO participants (name, contribution, credit_history, user_id) VALUES (%s, %s, %s, %s)",
            (person.name, person.contribution, person.credit_history, user_id)
        )
        self.db_conn.commit()

    def choose_winner(self):
        winner = random.choice(self.participants)
        winner_index = self.participants.index(winner)
        self.cursor.execute(
            "UPDATE participants SET chosen = TRUE WHERE id = %s",
            (winner_index + 1,)
        )
        self.db_conn.commit()
        return winner
