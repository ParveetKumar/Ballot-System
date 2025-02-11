CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE participants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contribution DECIMAL NOT NULL,
    credit_history VARCHAR(255),
    user_id INTEGER REFERENCES users(user_id),
    chosen BOOLEAN DEFAULT FALSE
);

CREATE TABLE repayments (
    repayment_id SERIAL PRIMARY KEY,
    participant_id INTEGER REFERENCES participants(id),
    total_amount DECIMAL NOT NULL,
    months INTEGER NOT NULL,
    monthly_emi DECIMAL NOT NULL
);

CREATE TABLE payment_history (
    payment_id SERIAL PRIMARY KEY,
    repayment_id INTEGER REFERENCES repayments(repayment_id),
    payment_date DATE NOT NULL,
    payment_amount DECIMAL NOT NULL
);
