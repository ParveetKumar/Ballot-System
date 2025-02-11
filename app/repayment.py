from datetime import date

class RepaymentPlan:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.cursor = db_conn.cursor()

    def create_plan(self, participant_id, total_amount, months):
        emi = total_amount / months
        self.cursor.execute(
            "INSERT INTO repayments (participant_id, total_amount, months, monthly_emi) VALUES (%s, %s, %s, %s)",
            (participant_id, total_amount, months, emi)
        )
        self.db_conn.commit()

    def add_payment(self, repayment_id, amount):
        today = date.today()
        self.cursor.execute(
            "INSERT INTO payment_history (repayment_id, payment_date, payment_amount) VALUES (%s, %s, %s)",
            (repayment_id, today, amount)
        )
        self.db_conn.commit()
