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


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():

    sql_create_student_table = """ CREATE TABLE IF NOT EXISTS student (
                                        student_id integer PRIMARY KEY AUTOINCREMENT,
                                        roll_number text NOT NULL UNIQUE,
                                        first_name text NOT NULL,
                                        last_name text
                                    ); """

    sql_create_course_table = """CREATE TABLE IF NOT EXISTS course (
                                    course_id integer PRIMARY KEY AUTOINCREMENT,
                                    course_code text NOT NULL UNIQUE,
                                    course_name text NOT NULL,
                                    course_description text
                                );"""

    sql_create_enrollments_table = """CREATE TABLE IF NOT EXISTS enrollments (
                                    enrollment_id integer PRIMARY KEY AUTOINCREMENT,
                                    estudent_id integer NOT NULL,
                                    ecourse_id integer NOT NULL,
                                    FOREIGN KEY (estudent_id) REFERENCES student (student_id)
                                    FOREIGN KEY (ecourse_id) REFERENCES course (course_id)
                                );"""

    # create a database connection
    conn = create_connection('database.sqlite3')

    # create tables
    if conn is not None:
        # create student table
        create_table(conn, sql_create_student_table)

        # create course table
        create_table(conn, sql_create_course_table)

        # create enrollments table
        create_table(conn, sql_create_enrollments_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
