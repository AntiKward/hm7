import sqlite3

class LibraryDatabase:
  def __init__(self, db_name="library.db"):
    self.connection = sqlite3.connect(db_name)
    self.cursor = self.connection.cursor()
    self.create_table()

  def create_table(self):
    self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
          )
      """)
    self.connection.commit()

  def add_book(self, title, author, year):
    self.cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    self.connection.commit()

  def close(self):
    self.connection.close()

library_db = LibraryDatabase()
library_db.add_book('Книга', 'Я', 2024)
library_db.close()
