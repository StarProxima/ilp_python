import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('SQL_Students.db')
        return con
        print("Соединение работает")
    except Error:
        print(Error)

# CREATE TABLE Сhiefs
# (	СhiefID int PRIMARY KEY identity(1,1) not for replication not null,
# 	FIO varchar(100) NOT NULL,
# 	WorkExperience int NOT NULL )

# CREATE TABLE Posts
# (	PostID int PRIMARY KEY identity(1,1) not for replication not null,
# 	Name varchar(100) NOT NULL,
# 	Location varchar(100) NOT NULL )

# CREATE TABLE Guards
# (	GuardID int PRIMARY KEY identity(1,1) not for replication not null,
# 	СhiefID int NOT NULL,
# 	FIO varchar(100) NOT NULL,
# 	WorkExperience int NOT NULL )

# CREATE TABLE OnDuty
# (	OnDutyID int PRIMARY KEY identity(1,1) not for replication not null,
# 	GuardID int NOT NULL,
# 	PostID int NOT NULL,
# 	СhiefID int NOT NULL,
# 	ExitTime DateTime NOT NULL )

# CREATE TABLE Remarks
# (	RemarkID int PRIMARY KEY identity(1,1) not for replication not null,
# 	GuardID int NOT NULL,
# 	PostID int NOT NULL,
# 	СhiefID int NOT NULL,
# 	Remark varchar(100) NOT NULL )


# "FOREIGN KEY (FacultyID) REFERENCES Faculties(FacultyID),"
#
# "FOREIGN KEY (SpecialtyID) REFERENCES Specialities(SpecialtyID),"
#
# "FOREIGN KEY (SetID) REFERENCES Sets(SetID),"
# "FOREIGN KEY (TeachFormID) REFERENCES TeachForm(TeachFormID),"
#
# "FOREIGN KEY (GroupID) REFERENCES Groups(GroupID),"

def sql_faculties(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Faculties("
        "FacultyID integer PRIMARY KEY,"
        "FacultyName text,"
        "Descript text)")

    cursorObj.execute(
        "INSERT INTO Faculties "
        "VALUES(1, 'ФКТиПМ', 'Факультет питона')"
    )
    cursorObj.execute(
        "INSERT INTO Faculties "
        "VALUES(2, 'РГФ', 'Гуманитарии')"
    )

    cursorObj.execute(
        "INSERT INTO Faculties "
        "VALUES(3, 'Журфак', 'Бесполезнарии')"
    )
    con.commit()


def sql_specialities(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Specialties("
        "SpecialtyID integer PRIMARY KEY,"
        "FacultyID integer,"

        "SpecialtyName text,"
        "SpecialtyCode integer,"
        "Descript text)")
    con.commit()


def sql_sets(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Sets(SetID integer PRIMARY KEY,"
        "SpecialtyID integer,"

        "SetName text,"
        "SetYear text)")
    con.commit()


def sql_teach_form(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE TeachForm("
        "TeachFormID integer PRIMARY KEY,"
        "Descript text)")
    con.commit()


def sql_groups(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Groups("
        "GroupID integer PRIMARY KEY,"

        "TeachFormID integer,"

        "GroupName text)")
    con.commit()


def sql_students(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Students("
        "StudentID integer PRIMARY KEY,"
        "GroupID integer,"

        "Surname text,"
        "Firstname text,"
        "Lastname text,"
        "Phone text)")
    con.commit()


def select(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table = cursorObj.fetchall()

    tablesList = []
    for tab in table:
        tablesList.append(tab[0])

    for listItem in tablesList:
        print(f"Вывод содержимого таблицы {listItem}")
        cursorObj.execute(f'SELECT * from {listItem}')
        [print(row) for row in cursorObj.fetchall()]


def sql_update(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        'UPDATE Faculties SET FacultyName = "ФКТ" where FacultyID = 1')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute(
        'UPDATE Faculties SET FacultyName = "ФРГ" where FacultyID = 2')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute(
        'UPDATE Faculties SET FacultyName = "Журналисты" where FacultyID = 3')
    con.commit()


def sql_delete(con):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE from Faculties where FacultyID = 3')
    con.commit()


# con = sql_connection()
#
# sql_faculties(con)
# sql_specialities(con)
# sql_sets(con)
# sql_teach_form(con)
# sql_groups(con)
# sql_students(con)
#
# select(con)
# print("ВЫВОД АПДЕЙТА")
# sql_update(con)
# select(con)
# print("ВЫВОД УДАЛЕНИЯ")
# sql_delete(con)
# select(con)
