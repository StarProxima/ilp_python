# предметная область - косметика
# придумать три таблицы
# таблицы дожны состоять больше чем из 2
# таблицы должны быть между собой связаны
# и написать запросы
import sqlite3
import os
from sqlite3 import Error


# cur = con.cursor()
tables_whitelist = [
    'brends',
    'stocks',
    'produkts'
]


def sql_connection():
    try:
        connnect = sqlite3.connect('SQL_SecurityService.db')
        return connnect
    except Error:
        print(Error)


def check_create(connnect):
    cur = connnect.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return cur.fetchall().__len__() == 5


def chiefs_table(connnect):
    cur = connnect.cursor()
    cur.execute(
        "CREATE TABLE Chiefs("
        "ChiefID INTEGER PRIMARY KEY,"
        "FIO varchar(100) NOT NULL,"
        "WorkExperience INTEGER NOT NULL )")
    connnect.commit()


def posts_table(connnect):
    cur = connnect.cursor()
    cur.execute(
        "CREATE TABLE Posts("
        "PostID INTEGER PRIMARY KEY,"
        "Name varchar(100) NOT NULL,"
        "Location varchar(100) NOT NULL )")
    connnect.commit()


def guards_table(connnect):
    cur = connnect.cursor()
    cur.execute(
        "CREATE TABLE Guards("
        "GuardID INTEGER PRIMARY KEY,"
        "ChiefID INTEGER NOT NULL REFERENCES Chiefs(ChiefID) ON UPDATE CASCADE,"
        "FIO varchar(100) NOT NULL,"
        "WorkExperience INTEGER NOT NULL )")
    connnect.commit()


def onduty_table(connnect):
    cur = connnect.cursor()
    cur.execute(
        "CREATE TABLE OnDuty("
        "OnDutyID INTEGER PRIMARY KEY,"
        "GuardID INTEGER NOT NULL REFERENCES Guards(GuardID) ON UPDATE CASCADE,"
        "PostID INTEGER NOT NULL REFERENCES Posts(PostID) ON UPDATE CASCADE,"
        "ChiefID INTEGER NOT NULL REFERENCES Chiefs(ChiefID) ON UPDATE CASCADE,"
        "ExitTime DateTime NOT NULL )")
    connnect.commit()


def remarks_table(connnect):
    cur = connnect.cursor()
    cur.execute(
        "CREATE TABLE Remarks("
        "RemarkID INTEGER PRIMARY KEY,"
        "GuardID INTEGER NOT NULL REFERENCES Guards(GuardID) ON UPDATE CASCADE,"
        "PostID INTEGER NOT NULL REFERENCES Posts(PostID) ON UPDATE CASCADE,"
        "ChiefID INTEGER NOT NULL REFERENCES Chiefs(ChiefID) ON UPDATE CASCADE,"
        "Remark varchar(100) NOT NULL )")
    connnect.commit()


connect = sql_connection()


def setup_tables():
    if not check_create(connect):
        chiefs_table(connect)
        posts_table(connect)
        guards_table(connect)
        onduty_table(connect)
        remarks_table(connect)
        print("Tables created")
    else:
        print("Tables already exist")


def add_test_data():
    cur = connect.cursor()

    # check if data exist

    if cur.fetchall().__len__() > 0:
        print("Data already exist")
        return

    cur.execute("""
        INSERT INTO Chiefs VALUES
        (1, 'Иванов И.И.', 5),
        (2, 'Петров П.П.', 10),
        (3, 'Сидоров С.С.', 15)
    """)

    cur.execute("""
        INSERT INTO Posts(PostID, Name, Location) VALUES
        (1, 'Пост 1', 'Москва'),
        (2, 'Пост 2', 'Санкт-Петербург'),
        (3, 'Пост 3', 'Казань')
    """)

    cur.execute("""
        INSERT INTO Guards(GuardID, ChiefID, FIO, WorkExperience) VALUES
        (1, 1, 'Пупкин П.П.', 5),
        (2, 2, 'Алексеев А.А.', 10),
        (3, 3, 'Васильев В.В.', 15)
    """)

    cur.execute("""
        INSERT INTO OnDuty(OnDutyID, GuardID, PostID, ChiefID, ExitTime) VALUES
        (1, 1, 1, 1, '2022-07-21 00'),
        (2, 2, 2, 2, '2022-08-07 00'),
        (3, 3, 3, 3, '2020-08-25 00')
    """)

    cur.execute("""
        INSERT INTO Remarks(RemarkID, GuardID, PostID, ChiefID, Remark) VALUES
        (1, 1, 1, 1, 'Проспал'),
        (2, 2, 2, 2, 'Опоздал'),
        (3, 3, 3, 3, 'Курил на рабочем месте')
    """)

    connect.commit()


def get_all_chiefs():
    cur = connect.cursor()
    cur.execute("SELECT * FROM Chiefs")
    data = cur.fetchall()
    for d in data:
        print(d)

    cur.close()
    return data


def get_all_posts():
    cur = connect.cursor()
    cur.execute("SELECT * FROM Posts")
    data = cur.fetchall()
    for d in data:
        print(d)

    cur.close()
    return data


def get_all_guards():
    cur = connect.cursor()
    cur.execute("SELECT * FROM Guards")
    data = cur.fetchall()
    for d in data:
        print(d)

    cur.close()
    return data


def get_all_guards_joined():
    cur = connect.cursor()
    cur.execute(
        "SELECT GuardID, Chiefs.FIO, Guards.FIO, Guards.WorkExperience  FROM Guards JOIN Chiefs ON Guards.ChiefID == Chiefs.ChiefID")
    data = cur.fetchall()
    for d in data:
        print(d)

    cur.close()
    return data


def get_all_onduty():
    cur = connect.cursor()
    cur.execute("SELECT * FROM OnDuty")
    data = cur.fetchall()
    for d in data:
        print(d)

    cur.close()
    return data


def get_all_onduty_joined():
    cur = connect.cursor()
    cur.execute(
        "SELECT OnDutyID, Guards.FIO, Posts.Name, Chiefs.FIO, OnDuty.ExitTime FROM OnDuty JOIN Chiefs ON OnDuty.ChiefID == Chiefs.ChiefID JOIN Guards ON OnDuty.GuardID == Guards.GuardID JOIN Posts ON OnDuty.PostID == Posts.PostID")
    data = cur.fetchall()
    for d in data:
        print(d)

    cur.close()
    return data


def get_all_remarks():
    cur = connect.cursor()
    cur.execute("SELECT * FROM Remarks")
    data = cur.fetchall()
    for d in data:
        print(d)

    cur.close()
    return data


def get_all_remarks_joined():
    cur = connect.cursor()
    cur.execute(
        "SELECT RemarkID, Guards.FIO, Posts.Name, Chiefs.FIO, Remark FROM Remarks JOIN Chiefs ON Remarks.ChiefID == Chiefs.ChiefID JOIN Guards ON Remarks.GuardID == Guards.GuardID JOIN Posts ON Remarks.PostID == Posts.PostID")
    data = cur.fetchall()
    for d in data:
        print(d)

    cur.close()
    return data


# def get_all_chiefs_joined():
#     cur = connect.cursor()
#     cur.execute("""
#         SELECT ChiefID, FIO, WorkExperience, PostID, PostName, Location
#         FROM Chiefs
#         JOIN Posts ON Chiefs.ChiefID == Posts.ChiefID
#     """)
#     data = cur.fetchall()
#     for d in data:
#         print(d)

#     cur.close()
#     return data


# def get_all_product_joined():
#     cur = con.cursor()
#     cur.execute('''
#         select name_product, catagory, type,  name_brend, name_stock from product
#         JOIN brend on product.id_brend==brend.id_brend
#         JOIN stock on product.id_stock==stock.id_stock
#     ''')
#     data = cur.fetchall()
#     # for d in data:
#     # print(d)

#     cur.close()
#     return data


# def get_all_brend_joined():
#     cur = con.cursor()
#     cur.execute('''
#         select id_brend,name_brend, country from brend
#     ''')
#     data = cur.fetchall()
#     # for d in data:
#     # print (d)
#     cur.close()
#     return data


# def get_all_kk_joined():
#     cur = con.cursor()
#     cur.execute('''
#         SELECT id_stock, name_stock, start_stock, finish_stock, percent_stock from stock
# ''')
#     data = cur.fetchall()
#     # for d in data:
#     #   print (d)
#     cur.close()
#     return data


def execute_fetch(sql):  # новая функция
    cur = connect.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    return data


def execute_insert_commit(sql, data):  # новая функция
    cur = connect.cursor()
    cur.execute(sql, data)
    connect.commit()


def add_guard(ChiefId, Fio, WorkExperience):
    sql = """
        INSERT INTO Guards (ChiefId, Fio, WorkExperience) VALUES (?, ?, ?)
    """
    data = (ChiefId, Fio, WorkExperience)
    execute_insert_commit(sql, data)


def add_chief(Fio, WorkExperience):
    sql = """
        INSERT INTO Chiefs (Fio, WorkExperience) VALUES (?, ?)
    """
    data = (Fio, WorkExperience)
    execute_insert_commit(sql, data)


def add_post(Name, Location):
    sql = """
        INSERT INTO Posts (Name, Location) VALUES (?, ?)
    """
    data = (Name, Location)
    execute_insert_commit(sql, data)


def add_onduty(ChiefId, GuardId, PostId, ExitTime):
    sql = """
        INSERT INTO OnDuty (ChiefId, GuardId, PostId, ExitTime) VALUES (?, ?, ?, ?)
    """
    data = (ChiefId, GuardId, PostId, ExitTime)
    execute_insert_commit(sql, data)


def add_remark(ChiefId, GuardId, PostId, Remark):
    sql = """
        INSERT INTO Remarks (ChiefId, GuardId, PostId, Remark) VALUES (?, ?, ?, ?)
    """
    data = (ChiefId, GuardId, PostId, Remark)
    execute_insert_commit(sql, data)
