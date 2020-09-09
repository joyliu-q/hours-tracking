import sqlite3

connection = sqlite3.connect("main.db")
cursor = connection.cursor()

class Member:
    def __init__(self, first_name, last_name, class_of, email, paid_dues):
        self.first_name = first_name
        self.last_name = last_name
        self.class_of = class_of
        self.email = email
        self.paid_dues = paid_dues
        self.auth_admin = False

def insert_member(member):
    cursor.execute('INSERT INTO members VALUES (?,?,?,?,?, ?)', 
        (member.first_name, member.last_name, member.class_of, member.email, 
        member.paid_dues, member.auth_admin))

def insert_bulk_member(members):
    bulk = []
    for member in members:
        bulk.append((member.first_name, member.last_name, member.class_of, member.email, 
        member.paid_dues, member.auth_admin))
    cursor.executemany('INSERT INTO members VALUES (?,?,?,?,?)', bulk)

def return_paid_dues(dues_bool):
    cursor.execute("SELECT * FROM members WHERE paid_dues = '%s'" % dues_bool)
    print(cursor.fetchall())

def return_all_members():
    cursor.execute("SELECT * FROM members")
    print(cursor.fetchall())

bob = Member("Bob", "TheBuilder", "2020", "bobthebuilder@gmail.com", True)
insert_member(bob)
return_paid_dues("1")
