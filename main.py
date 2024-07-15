import sqlite3
import time

def input_handler():
    query_number = int(input("Enter SQL-query number (from 1 to 12): "))
    print(list_of_queries[int(f"{query_number}")-1])
    sql_file = f"query_{query_number}.sql"
    time.sleep(3) # щоб можна було встигнути помітити і прочитати умову завдання :-)
    if query_number == 1 or query_number == 4:
        execute_sql_file_0("university.db", sql_file)
    elif query_number == 2 or query_number == 3:
        id = input("Enter subject_id (from 1 to 8): ")
        execute_sql_file_1("university.db", sql_file, id)
    elif query_number == 5:
        id = input("Enter teacher_id (from 1 to 5): ")
        execute_sql_file_1("university.db", sql_file, id)
    elif query_number == 6:
        id = input("Enter group_id (from 1 to 3): ")
        execute_sql_file_1("university.db", sql_file, id)
    elif query_number == 7:
        group_id = input("Enter group_id (from 1 to 3): ")
        subject_id = input("Enter subject_id (from 1 to 8): ")
        execute_sql_file_2("university.db", sql_file, group_id, subject_id)
    elif query_number == 8:
        id = input("Enter teacher_id (from 1 to 5): ")
        execute_sql_file_1("university.db", sql_file, id)
    elif query_number == 9:
        id = input("Enter student_id (from 1 to 50): ")
        execute_sql_file_1("university.db", sql_file, id)
    elif query_number == 10:
        student_id = input("Enter student_id (from 1 to 50): ")
        teacher_id = input("Enter teacher_id (from 1 to 5): ")
        execute_sql_file_2("university.db", sql_file, student_id, teacher_id)
    elif query_number == 11:
        teacher_id = input("Enter teacher_id (from 1 to 5): ")
        student_id = input("Enter student_id (from 1 to 50): ")
        execute_sql_file_2("university.db", sql_file, teacher_id, student_id)
    elif query_number == 12:
        group_id = input("Enter group_id (from 1 to 3): ")
        subject_id1 = input("Enter subject_id (from 1 to 8): ")
        subject_id2 = subject_id1    
        execute_sql_file_3("university.db", sql_file, group_id, subject_id1, subject_id2)
    else:
        print(f"Query {query_number} is out of the available list, try again.")
        

def execute_sql_file_0(database, sql_file): # для запитів 1 і 4
    with open(sql_file, 'r') as file:
        sql_query = file.read()

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        for row in results:
            print(row)


# для запитів 2, 3, 5, 6, 8, 9 (тих, де потрібено вказувати 1 параметр)
def execute_sql_file_1(database, sql_file, id): 
    with open(sql_file, 'r') as file:
        sql_query = file.read()

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_query, (id, ))
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("Incorrect parameters, plese check")


# для запитів номер  7, 10 та 11 (тих, де потрібено вказувати 2 параметри)
def execute_sql_file_2(database, sql_file, id1, id2):
    with open(sql_file, 'r') as file:
        sql_query = file.read()

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_query, (id1, id2))
        results = cursor.fetchall()
        if results:
            for row in results:
                if row == (None,):
                    print("Incorrect parameters, plese check")
                else:
                    print(row)
        else:
            print("Incorrect parameters, plese check")


# для запитів номер 12 (де потрібено вказувати 3 параметри)
def execute_sql_file_3(database, sql_file, id1, id2, id3):
    with open(sql_file, 'r') as file:
        sql_query = file.read()

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_query, (id1, id2, id3))
        results = cursor.fetchall()
        if results:
            for row in results:
                if row == (None,):
                    print("Incorrect parameters, plese check")
                else:
                    print(row)
        else:
            print("Incorrect parameters, plese check")


list_of_queries = ["1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.", 
                   "2. Знайти студента із найвищим середнім балом з певного предмета.",
                   "3. Знайти середній бал у групах з певного предмета.", 
                   "4. Знайти середній бал на потоці (по всій таблиці оцінок).", 
                   "5. Знайти які курси читає певний викладач.", 
                   "6. Знайти список студентів у певній групі.",
                   "7. Знайти оцінки студентів у окремій групі з певного предмета.",
                   "8. Знайти середній бал, який ставить певний викладач зі своїх предметів.",
                   "9. Знайти список курсів, які відвідує студент.",
                   "10. Список курсів, які певному студенту читає певний викладач.",
                   "11. Середній бал, який певний викладач ставить певному студентові.",
                   "12. Оцінки студентів у певній групі з певного предмета на останньому занятті."
                   ]


if __name__ == "__main__":
    input_handler()
