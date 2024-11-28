import sqlite3


def get_items(sort: str):
    ans = []
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    match sort:
        case 'name':
            lst = cur.execute('SELECT name, imgUrl, desc, price FROM Items').fetchall()
            lst = sorted(lst, key=lambda x: x[0])
            for id, i in enumerate(lst):
                item = {
                    'id': id,
                    'name': i[0],
                    'imgUrl': i[1],
                    'desc': i[2].split("%%%"),
                    'price': i[3],
                }
                ans.append(item)
        case 'price':
            lst = cur.execute('SELECT name, imgUrl, desc, price FROM Items').fetchall()
            lst = sorted(lst, key=lambda x: x[3])
            for id, i in enumerate(lst):
                item = {
                    'id': id,
                    'name': i[0],
                    'imgUrl': i[1],
                    'desc': i[2].split("%%%"),
                    'price': i[3],
                }
                ans.append(item)
        case '-price':
            lst = cur.execute('SELECT name, imgUrl, desc, price FROM Items').fetchall()
            lst = sorted(lst, key=lambda x: x[3], reverse=True)
            for id, i in enumerate(lst):
                item = {
                    'id': id,
                    'name': i[0],
                    'imgUrl': i[1],
                    'desc': i[2].split("%%%"),
                    'price': i[3],
                }
                ans.append(item)
    return ans


def create_item(name: str, imgurl: str, desc: list, price: int):
    desc = '%%%'.join(desc)
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO Items VALUES (?, ?, ?, ?)', (name, imgurl, desc, price))
    conn.commit()
    conn.close()


def create_order(items: list, total_price: int):
    ans = [i["name"] for i in items]
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO Orders VALUES (?, ?)', ("%%%".join(ans), total_price))
    conn.commit()
    conn.close()


def auth(username: str, password: str):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    ans = cur.execute('SELECT password FROM Admins WHERE username = ?', (username,)).fetchall()
    if ans[0][0] == password:
        return True
    else:
        return False