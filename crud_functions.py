import sqlite3

def initiate_db(db_name='products.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    title = ['product1', 'product2', 'product3', 'product4']
    description = ['описание1', 'описание2', 'описание3', 'описание4']
    price = ['5000', '10000', '15000', '20000']

    cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
                   (f'{title[0]}', f'{description[0]}', f'{price[0]}'))
    cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
                   (f'{title[1]}', f'{description[1]}', f'{price[1]}'))
    cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
                   (f'{title[2]}', f'{description[2]}', f'{price[2]}'))
    cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
                   (f'{title[3]}', f'{description[3]}', f'{price[3]}'))
    conn.commit()
    conn.close()

def get_all_products(db_name='products.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()

    return products

if __name__ == '__main__':
    initiate_db()
    products = get_all_products()
    for product in products:
        print(product)
