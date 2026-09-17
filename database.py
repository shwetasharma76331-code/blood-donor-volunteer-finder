import sqlite3
def create_database():
    conn = sqlite3.connect("bloodconnect.db")
    cursor = conn.cursor()
    cursor.execute("""
          CREATE TABLE IF NOT
EXISTS donors(
               id TEXT NOT NULL,
KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                blood_group TEXT
NOT NULL,
                city TEXT NOT NULL,
                phone TEXT NOT NULL
             )
         """)
    conn.commit()
    conn.close()
if __name__=="__main__":
    create_database()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

