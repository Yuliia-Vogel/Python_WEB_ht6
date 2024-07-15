# робочий файл, яким я створювала базу, таблички в ній та заповнювала таблички, 
# по черзі вносячи в точку входу то одну функці, то іншу, залежно від того, 
# що слід було зробити в той момент

import sqlite3
import random
from faker import Faker
from datetime import datetime, timedelta

from connection import create_connection


fake_data = Faker("uk-UA")
COUNTER = 50

list_of_subjects = ['Mathematics', 'English', 'Ukrainian', 'Biology', 'Geography', 'Chemistry', 'Physics', 'History']

def insert_students(connection):
    cursor = connection.cursor()
    sql_query = "INSERT INTO students (first_name, last_name) VALUES (?, ?)"
    students = [(fake_data.first_name(), fake_data.last_name()) for _ in range(COUNTER)]
    cursor.executemany(sql_query, students)
    connection.commit()


def insert_teachers(connection):
    cursor = connection.cursor()
    sql_query = "INSERT INTO teachers (first_name, last_name) VALUES (?, ?)"
    teachers = [(fake_data.first_name(), fake_data.last_name()) for _ in range(5)]
    cursor.executemany(sql_query, teachers)
    connection.commit()


def create_table_teachers(database, table_name): # teachers
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                teacher_id_pk INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR(30),
                last_name VARCHAR(30)
            )
        """)


def create_table_subjects(database, table_name): # subjects
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                subject_id_pk INTEGER PRIMARY KEY AUTOINCREMENT,
                sub_name_u VARCHAR(50) UNIQUE, 
                teacher_id_fk INTEGER,
                FOREIGN KEY (teacher_id_fk) REFERENCES teachers (teacher_id_pk)
            )
        """)


def create_table_marks(database, table_name): # marks
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                student_id_fk INTEGER,
                subject_id_fk INTEGER,
                mark INTEGER, 
                creation_date TIMESTAMP,
                FOREIGN KEY (student_id_fk) REFERENCES students (student_id_pk),
                FOREIGN KEY (subject_id_fk) REFERENCES subjects (subject_id_pk)
            )
        """)


def random_date(start, end):
    """Генерує випадкову дату між двома датами."""
    delta = end - start
    random_days = random.randint(0, delta.days)
    random_date = start + timedelta(days=random_days)
    random_seconds = random.randint(0, 86399)  # Кількість секунд в добі
    random_date_time = random_date + timedelta(seconds=random_seconds)
    return random_date_time.strftime("%Y-%m-%d %H:%M:%S")


def insert_marks(database):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()

        # Витягуємо всі student_id_pk з таблиці students
        cursor.execute("SELECT student_id_pk FROM students")
        students = cursor.fetchall()

        # Витягуємо всі subject_id_pk з таблиці subjects
        cursor.execute("SELECT subject_id_pk FROM subjects")
        subjects = cursor.fetchall()

        # Дати початку і кінця періоду
        start_date = datetime(2024, 3, 1)
        end_date = datetime(2024, 4, 30)

        # Підготовка даних для вставки
        marks_data = []
        for student in students:
            for subject in subjects:
                for _ in range(2):  # Кожен студент має 2 оцінки з кожного предмету, загалом 16 оцінок
                    student_id = student[0]
                    subject_id = subject[0]
                    mark = random.randint(1, 100)
                    creation_date = random_date(start_date, end_date)
                    marks_data.append((student_id, subject_id, mark, creation_date))

        # Вставка даних у таблицю marks
        cursor.executemany("INSERT INTO marks (student_id_fk, subject_id_fk, mark, creation_date) VALUES (?, ?, ?, ?)", marks_data)
        conn.commit()


# def create_table_group_lists(database): # students
#     with sqlite3.connect(database) as conn:
#         cursor = conn.cursor()
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS group_lists (
#                 group_id_fk INTEGER,
#                 student_id_fk INTEGER,
#                 FOREIGN KEY (group_id_fk) REFERENCES group_numbers(group_id_pk),
#                 FOREIGN KEY (student_id_fk) REFERENCES students(student_id_pk)
#             )
#         """)


def add_column(database, table_name, column_name):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(f"ALTER TABLE {table_name} ADD {column_name}")

def insert_data(database, table_name):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {table_name} (group_number) VALUES (3)")

def clear_table(database, table_name):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table_name}")

def drop_table(database, table_name):
     with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE {table_name}")

def select(database):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM group_lists WHERE group_id_fk=3")
        results = cursor.fetchall()
        print(len(results))
        for row in results:
            print(row)



def distribute_students():
    with sqlite3.connect("university.db") as conn:
        cursor = conn.cursor()
        
        # Витягуємо усіх студентів
        cursor.execute("SELECT student_id_pk FROM students")
        students = cursor.fetchall()
        
        # Витягуємо усі групи
        cursor.execute("SELECT group_id_pk FROM group_no")
        groups = cursor.fetchall()
        
        # Розподіл студентів між групами
        student_group_pairs = []
        group_count = len(groups)
        
        for i, student in enumerate(students):
            group_id = groups[i % group_count][0]  # Вибираємо групу на основі індексу
            student_id = student[0]
            student_group_pairs.append((group_id, student_id))
        
        # Вставляємо дані у таблицю group_lists
        cursor.executemany("INSERT INTO group_lists (group_id_fk, student_id_fk) VALUES (?, ?)", student_group_pairs)
        conn.commit()


def insert_subjects_and_teachers(database, list_of_subjects):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()

        # Витягуємо всі teacher_id_pk з таблиці teachers
        cursor.execute("SELECT teacher_id_pk FROM teachers")
        teachers = cursor.fetchall()

        # Підготовка даних для вставки
        subjects_data = []
        for subject in list_of_subjects:
            teacher_id = random.choice(teachers)[0]  # Вибираємо перший елемент з кортежу  # Випадковий вибір teachers
            subjects_data.append((subject, teacher_id))

        # Вставка даних у таблицю subjects
        cursor.executemany("INSERT INTO subjects (sub_name_u, teacher_id_fk) VALUES (?, ?)", subjects_data)
        conn.commit()



if __name__ == "__main__":
    database = "university.db"
    table_name = "marks"
    insert_marks(database)
    # clear_table(database, table_name)
    print(f"{table_name} table has been changed.")


# if __name__ == "__main__": # точка входу для функцій insert_teachers(conn) та insert_students(conn)
#     database = './university.db'
#     with create_connection(database) as conn:
#         insert_teachers(conn)
