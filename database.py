import sqlite3
DB_NAME = "bloodconnect.db"


def get_connection():
    return
sqlite3.connect(DB_NAME)
def create_database():
 conn = sqlite3.connect(DB_NAME)
 cursor = conn.cursor()

 cursor.execute("""
        CREATE TABLE IF NOT EXISTS donors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            blood_group TEXT NOT NULL,
            city TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)

 conn.commit()
 conn.close()

def add_donor(name, age, blood_group, city, phone):
    conn = sqlite3.connect("bloodconnect.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO donors (name, age, blood_group, city, phone)
        VALUES (?, ?, ?, ?, ?)
    """, (name, age, blood_group, city, phone))

    conn.commit()
    conn.close()


def get_donors():
    conn = sqlite3.connect("bloodconnect.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()

    conn.close()
    return donors
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

