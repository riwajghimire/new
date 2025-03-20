import sqlite3
import json
datas = [
    {"title": "A Light in the Attic", "currency": "£", "price": "51.77"},
    {"title": "Tipping the Velvet", "currency": "£", "price": "53.74"},
    {"title": "Soumission", "currency": "£", "price": "50.10"},
    {"title": "Sharp Objects", "currency": "£", "price": "47.82"},
    {"title": "Sapiens: A Brief History of Humankind", "currency": "£", "price": "54.23"},
    {"title": "The Requiem Red", "currency": "£", "price": "22.65"},
    {"title": "The Dirty Little Secrets of Getting Your Dream Job", "currency": "£", "price": "33.34"},
    {"title": "The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull", "currency": "£", "price": "17.93"},
    {"title": "The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics", "currency": "£", "price": "22.60"},
    {"title": "The Black Maria", "currency": "£", "price": "52.15"},
    {"title": "Starving Hearts (Triangular Trade Trilogy, #1)", "currency": "£", "price": "13.99"},
    {"title": "Shakespeare's Sonnets", "currency": "£", "price": "20.66"},
    {"title": "Set Me Free", "currency": "£", "price": "17.46"},
    {"title": "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)", "currency": "£", "price": "52.29"},
    {"title": "Rip it Up and Start Again", "currency": "£", "price": "35.02"},
    {"title": "Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991", "currency": "£", "price": "57.25"},
    {"title": "Olio", "currency": "£", "price": "23.88"},
    {"title": "Mesaerion: The Best Science Fiction Stories 1800-1849", "currency": "£", "price": "37.59"},
    {"title": "Libertarianism for Beginners", "currency": "£", "price": "51.33"},
    {"title": "It's Only the Himalayas", "currency": "£", "price": "45.17"}
]
con = sqlite3.connect('books.db')
cur = con.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title varchar,
    currency vharchar,
    price float
)
''')
for data in datas:
    cur.execute('''
    INSERT INTO books (title, currency, price) VALUES (?, ?, ?)
    ''', (data['title'], data['currency'], float(data['price'])))

con.commit()
con.close()

