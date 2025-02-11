def fetch_one(cursor, query, params):
    cursor.execute(query, params)
    return cursor.fetchone()

def fetch_all(cursor, query, params):
    cursor.execute(query, params)
    return cursor.fetchall()
