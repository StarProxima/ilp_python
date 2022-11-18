import sqlite3
from sqlite3 import Error


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
        "ChiefID int PRIMARY KEY,"
        "FIO varchar(100) NOT NULL,"
        "WorkExperience int NOT NULL )")
    connnect.commit()


def posts_table(connnect):
    cur = connnect.cursor()
    cur.execute(
        "CREATE TABLE Posts("
        "PostID int PRIMARY KEY,"
        "Name varchar(100) NOT NULL,"
        "Location varchar(100) NOT NULL )")
    connnect.commit()


def guards_table(connnect):
    cur = connnect.cursor()
    cur.execute(
        "CREATE TABLE Guards("
        "GuardID int PRIMARY KEY,"
        "ChiefID int NOT NULL REFERENCES Chiefs(ChiefID) ON UPDATE CASCADE,"
        "FIO varchar(100) NOT NULL,"
        "WorkExperience int NOT NULL )")
    connnect.commit()


def onduty_table(connnect):
    cur = connnect.cursor()
    cur.execute(
        "CREATE TABLE OnDuty("
        "OnDutyID int PRIMARY KEY,"
        "GuardID int NOT NULL REFERENCES Guards(GuardID) ON UPDATE CASCADE,"
        "PostID int NOT NULL REFERENCES Posts(PostID) ON UPDATE CASCADE,"
        "ChiefID int NOT NULL REFERENCES Chiefs(ChiefID) ON UPDATE CASCADE,"
        "ExitTime DateTime NOT NULL )")
    connnect.commit()


def remarks_table(connnect):
    cur = connnect.cursor()
    cur.execute(
        "CREATE TABLE Remarks("
        "RemarkID int PRIMARY KEY,"
        "GuardID int NOT NULL REFERENCES Guards(GuardID) ON UPDATE CASCADE,"
        "PostID int NOT NULL REFERENCES Posts(PostID) ON UPDATE CASCADE,"
        "ChiefID int NOT NULL REFERENCES Chiefs(ChiefID) ON UPDATE CASCADE,"
        "Remark varchar(100) NOT NULL )")
    connnect.commit()


def insert_chiefs(connnect):
    cur = connnect.cursor()

    cur.execute("INSERT INTO Chiefs VALUES(1, 'Иванов И.И.', 5)")
    cur.execute("INSERT INTO Chiefs VALUES(2, 'Петров П.П.', 10)")
    cur.execute("INSERT INTO Chiefs VALUES(3, 'Сидоров С.С.', 15)")
    cur.execute("INSERT INTO Chiefs VALUES(4, 'Васильев В.В.', 20)")
    cur.execute("INSERT INTO Chiefs VALUES(5, 'Пупкин П.П.', 25)")
    cur.execute("INSERT INTO Chiefs VALUES(6, 'Семенов С.С.', 30)")
    cur.execute("INSERT INTO Chiefs VALUES(7, 'Алексеев А.А.', 35)")
    cur.execute("INSERT INTO Chiefs VALUES(8, 'Андреев А.А.', 40)")
    cur.execute("INSERT INTO Chiefs VALUES(9, 'Антонов А.А.', 45)")
    cur.execute("INSERT INTO Chiefs VALUES(10, 'Артемов А.А.', 50)")
    connnect.commit()


def insert_posts(connnect):
    cur = connnect.cursor()

    cur.execute("INSERT INTO Posts VALUES(1, 'Пост 1', 'Москва')")
    cur.execute(
        "INSERT INTO Posts VALUES(2, 'Пост 2', 'Санкт-Петербург')")
    cur.execute("INSERT INTO Posts VALUES(3, 'Пост 3', 'Новосибирск')")
    cur.execute("INSERT INTO Posts VALUES(4, 'Пост 4', 'Екатеринбург')")
    cur.execute(
        "INSERT INTO Posts VALUES(5, 'Пост 5', 'Нижний Новгород')")
    cur.execute("INSERT INTO Posts VALUES(6, 'Пост 6', 'Казань')")
    cur.execute("INSERT INTO Posts VALUES(7, 'Пост 7', 'Челябинск')")
    cur.execute("INSERT INTO Posts VALUES(8, 'Пост 8', 'Омск')")
    cur.execute("INSERT INTO Posts VALUES(9, 'Пост 9', 'Самара')")
    cur.execute(
        "INSERT INTO Posts VALUES(10, 'Пост 10', 'Ростов-на-Дону')")
    connnect.commit()


def insert_guards(connnect):
    cur = connnect.cursor()

    cur.execute("INSERT INTO Guards VALUES(1, 1, 'Иванов И.И.', 5)")
    cur.execute("INSERT INTO Guards VALUES(2, 2, 'Петров П.П.', 10)")
    cur.execute("INSERT INTO Guards VALUES(3, 3, 'Сидоров С.С.', 15)")
    cur.execute("INSERT INTO Guards VALUES(4, 4, 'Васильев В.В.', 20)")
    cur.execute("INSERT INTO Guards VALUES(5, 5, 'Пупкин П.П.', 25)")
    cur.execute("INSERT INTO Guards VALUES(6, 6, 'Семенов С.С.', 30)")
    cur.execute("INSERT INTO Guards VALUES(7, 7, 'Алексеев А.А.', 35)")
    cur.execute("INSERT INTO Guards VALUES(8, 8, 'Андреев А.А.', 40)")
    cur.execute("INSERT INTO Guards VALUES(9, 9, 'Антонов А.А.', 45)")
    cur.execute("INSERT INTO Guards VALUES(10, 10, 'Артемов А.А.', 50)")
    connnect.commit()


def insert_onduty(connnect):
    cur = connnect.cursor()

    cur.execute("INSERT INTO OnDuty VALUES(1, 1, 1, 1, '2020-01-01 00:00:00')")
    cur.execute("INSERT INTO OnDuty VALUES(2, 2, 2, 2, '2020-01-01 00:00:00')")
    cur.execute("INSERT INTO OnDuty VALUES(3, 3, 3, 3, '2020-01-01 00:00:00')")
    cur.execute("INSERT INTO OnDuty VALUES(4, 4, 4, 4, '2020-01-01 00:00:00')")
    cur.execute("INSERT INTO OnDuty VALUES(5, 5, 5, 5, '2020-01-01 00:00:00')")
    cur.execute("INSERT INTO OnDuty VALUES(6, 6, 6, 6, '2020-01-01 00:00:00')")
    cur.execute("INSERT INTO OnDuty VALUES(7, 7, 7, 7, '2020-01-01 00:00:00')")
    cur.execute("INSERT INTO OnDuty VALUES(8, 8, 8, 8, '2020-01-01 00:00:00')")
    cur.execute("INSERT INTO OnDuty VALUES(9, 9, 9, 9, '2020-01-01 00:00:00')")
    cur.execute(
        "INSERT INTO OnDuty VALUES(10, 10, 10, 10, '2020-01-01 00:00:00')")
    connnect.commit()


def insert_remarks(connnect):
    cur = connnect.cursor()

    cur.execute(
        "INSERT INTO Remarks VALUES(1, 1, 1, 1, 'Прибыл')")
    cur.execute(
        "INSERT INTO Remarks VALUES(2, 2, 2, 2, 'Прибыл')")
    cur.execute(
        "INSERT INTO Remarks VALUES(3, 3, 3, 3, 'Прибыл')")
    cur.execute(
        "INSERT INTO Remarks VALUES(4, 4, 4, 4, 'Прибыл')")
    cur.execute(
        "INSERT INTO Remarks VALUES(5, 5, 5, 5, 'Прибыл')")
    cur.execute(
        "INSERT INTO Remarks VALUES(6, 6, 6, 6, 'Прибыл')")
    cur.execute(
        "INSERT INTO Remarks VALUES(7, 7, 7, 7, 'Прибыл')")
    cur.execute(
        "INSERT INTO Remarks VALUES(8, 8, 8, 8, 'Прибыл')")
    cur.execute(
        "INSERT INTO Remarks VALUES(9, 9, 9, 9, 'Прибыл')")
    cur.execute(
        "INSERT INTO Remarks VALUES(10, 10, 10, 10, 'Прибыл')")
    connnect.commit()


def select_chiefs(connnect):
    cur = connnect.cursor()
    cur.execute("SELECT * FROM Chiefs")
    print("Chiefs:")
    for row in cur.fetchall():
        print(row)
    print("")

    cur.execute("SELECT * FROM Chiefs WHERE ChiefID = 1")
    print("First chief:")
    for row in cur.fetchall():
        print(row)
    print("")


def select_posts(connnect):
    cur = connnect.cursor()
    cur.execute("SELECT * FROM Posts")
    print("Posts:")
    for row in cur.fetchall():
        print(row)
    print("")

    cur.execute("SELECT * FROM Posts WHERE PostID = 1")
    print("First post:")
    for row in cur.fetchall():
        print(row)
    print("")


def select_guards(connnect):
    cur = connnect.cursor()
    cur.execute("SELECT * FROM Guards")
    print("Guards:")
    for row in cur.fetchall():
        print(row)
    print("")

    cur.execute("SELECT * FROM Guards WHERE GuardID = 1")
    print("First guard:")
    for row in cur.fetchall():
        print(row)
    print("")


def select_onduty(connnect):
    cur = connnect.cursor()
    cur.execute("SELECT * FROM OnDuty")
    print("OnDuty:")
    for row in cur.fetchall():
        print(row)
    print("")

    cur.execute("SELECT * FROM OnDuty WHERE OnDutyID = 1")
    print("First onduty:")
    for row in cur.fetchall():
        print(row)
    print("")


def select_remarks(connnect):
    cur = connnect.cursor()
    cur.execute("SELECT * FROM Remarks")
    print("Remarks:")
    for row in cur.fetchall():
        print(row)
    print("")

    cur.execute("SELECT * FROM Remarks WHERE RemarkID = 1")
    print("First remark:")
    for row in cur.fetchall():
        print(row)
    print("")


def update_chiefs(connnect):
    cur = connnect.cursor()
    cur.execute("UPDATE Chiefs SET FIO = 'Updated fio' WHERE ChiefID = 1")
    cur.execute("UPDATE Chiefs SET WorkExperience = 100 WHERE ChiefID = 1")
    connnect.commit()


def update_posts(connnect):
    cur = connnect.cursor()
    cur.execute("UPDATE Posts SET Name = 'Updated name' WHERE PostID = 1")
    cur.execute(
        "UPDATE Posts SET Location = 'Updated location' WHERE PostID = 1")
    connnect.commit()


def update_guards(connnect):
    cur = connnect.cursor()
    cur.execute("UPDATE Guards SET FIO = 'Updated fio' WHERE GuardID = 1")
    cur.execute("UPDATE Guards SET WorkExperience = 99 WHERE GuardID = 1")
    connnect.commit()


def update_onduty(connect):
    cur = connect.cursor()
    # update ExitTime
    cur.execute(
        "UPDATE OnDuty SET ExitTime = '2022-01-01 00:00:00' WHERE OnDutyID = 1")
    cur.execute(
        "UPDATE OnDuty SET ChiefID = 2 WHERE OnDutyID = 1")
    connect.commit()


def update_remarks(connect):
    cur = connect.cursor()
    cur.execute(
        "UPDATE Remarks SET Remark = 'Updated remark' WHERE RemarkID = 1")
    cur.execute(
        "UPDATE Remarks SET ChiefID = 2 WHERE RemarkID = 1")
    connect.commit()


def delete_chiefs(connnect):
    cur = connnect.cursor()
    cur.execute("DELETE FROM Chiefs WHERE ChiefID = 1")
    cur.execute("DELETE FROM Chiefs WHERE ChiefID = 2")
    connnect.commit()


def delete_posts(connnect):
    cur = connnect.cursor()
    cur.execute("DELETE FROM Posts WHERE PostID = 1")
    cur.execute("DELETE FROM Posts WHERE PostID = 2")
    connnect.commit()


def delete_guards(connnect):
    cur = connnect.cursor()
    cur.execute("DELETE FROM Guards WHERE GuardID = 1")
    cur.execute("DELETE FROM Guards WHERE GuardID = 2")
    connnect.commit()


def delete_onduty(connnect):
    cur = connnect.cursor()
    cur.execute("DELETE FROM OnDuty WHERE OnDutyID = 1")
    cur.execute("DELETE FROM OnDuty WHERE OnDutyID = 2")
    connnect.commit()


def delete_remarks(connnect):
    cur = connnect.cursor()
    cur.execute("DELETE FROM Remarks WHERE RemarkID = 1")
    cur.execute("DELETE FROM Remarks WHERE RemarkID = 2")
    connnect.commit()


def select_all(connnect):
    select_chiefs(connnect)
    select_posts(connnect)
    select_guards(connnect)
    select_onduty(connnect)
    select_remarks(connnect)


def update_all(connnect):
    print("Update")
    update_chiefs(connnect)
    update_posts(connnect)
    update_guards(connnect)
    update_onduty(connnect)
    update_remarks(connnect)


def delete_all(connnect):
    print("Delete")
    delete_remarks(connnect)
    delete_onduty(connnect)
    delete_guards(connnect)
    delete_chiefs(connnect)
    delete_posts(connnect)


connect = sql_connection()

connect.execute("PRAGMA foreign_keys = ON")

connect.commit()

connect.commit()

if (check_create(connect)):
    print("Tables already created")
else:
    chiefs_table(connect)
    posts_table(connect)
    guards_table(connect)
    onduty_table(connect)
    remarks_table(connect)

    insert_chiefs(connect)
    insert_posts(connect)
    insert_guards(connect)
    insert_onduty(connect)
    insert_remarks(connect)


select_all(connect)

update_all(connect)

select_all(connect)

delete_all(connect)

select_all(connect)
