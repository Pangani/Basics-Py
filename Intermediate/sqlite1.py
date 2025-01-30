import sqlite3

class Person():
    def __init__(self, id=None, first_name=None, last_name=None, age=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def clone_person(self, result):
        self.id = result[0]
        self.first_name = result[1]
        self.last_name = result[2]
        self.age = result[3]

conn = sqlite3.connect('mydata.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL
               )""")

# cursor.execute("""INSERT INTO persons
#                VALUES ('1','John', 'Smith', 24),
#                ('2','Milca', 'Kasuya', 30),
#                ('3','Alina', 'Mpanda', 30)""")


cursor.execute("""SELECT * FROM persons WHERE last_name = 'Kasuya'""")

person1 = Person()
person1.clone_person(cursor.fetchone())

print(person1.first_name)
print(person1.last_name)

person2 = Person("4", "Roy", "Chitan", 30)
cursor.execute("INSERT INTO persons VALUES (?, ?, ?, ?)", (person2.id, person2.first_name, person2.last_name, person2.age))

person2.clone_person(cursor.fetchone(3))

print(person2.first_name)
print(person2.last_name)

conn.commit()
conn.close()