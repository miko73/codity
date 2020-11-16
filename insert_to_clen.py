#!/usr/bin/python
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def main():
    # create a database connection
    conn = sqlite3.connect('../db.sqlite3')
    print("Opened database successfully")

    with conn:
       cursor = execute(
          "SELECT Jmeno, prijmeni, rodne_cislo, datum_narozeni, sportovcem_od from FO_zakladna_2019_uni")
       for row in cursor:
          print("Jmeno = ", row[0])
          print("Prijmen = ", row[1])
          print("RC = ", row[2])
          print("datum narozeni = ", row[3])
          print("sportovcem od = ", row[4])

          print(insert_string)
          print("\n")
          # conn.execute("INSERT INTO moviebook_clen (jmeno, prijmeni, rc, narozen, clenem_od) VALUES (row[0], row[1], row[2], row[3], row[4] )")
          #   conn.commit(self)
          act_clen_string =

          project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        project_id = create_project(conn, project)

        # tasks
        task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)


if __name__ == '__main__':
    main()
