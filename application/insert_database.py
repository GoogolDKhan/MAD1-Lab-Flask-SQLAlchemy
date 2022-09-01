import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_course(conn, course):
    sql = ''' INSERT INTO course(course_id,course_code,course_name,course_description)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, course)
    conn.commit()
    return cur.lastrowid


def main():

    # create a database connection
    conn = create_connection('database.sqlite3')
    with conn:

        # courses
        course_1 = (1, 'CSE01', 'MAD 1', 'Modern Application Development - I')
        course_2 = (2, 'CSE02', 'DBMS', 'Database management Systems')
        course_3 = (3, 'CSE03', 'PDSA', 'Programming, Data Structures and Algorithms using Python')
        course_4 = (4, 'BST13', 'BDM', 'Business Data Management')

        # create courses
        create_course(conn, course_1)
        create_course(conn, course_2)
        create_course(conn, course_3)
        create_course(conn, course_4)


if __name__ == '__main__':
    main()