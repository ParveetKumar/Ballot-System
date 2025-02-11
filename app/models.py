class Person:
    def __init__(self, name, contribution, credit_history):
        self.name = name
        self.contribution = contribution
        self.credit_history = credit_history

class Repayment:
    def __init__(self, participant_id, total_amount, months, emi):
        self.participant_id = participant_id
        self.total_amount = total_amount
        self.months = months
        self.emi = emi
