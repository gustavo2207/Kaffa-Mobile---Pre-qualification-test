import cx_Oracle
import os

os.chdir("C:")
os.chdir(r"C:\Users\gusta\Downloads\instantclient-basic-windows.x64-19.11.0.0.0dbru\instantclient_19_11")


def create_task(connection):
    cursor = connection.cursor()
    task = input("\nTask's name: ")

    try:
        cursor.execute(
            "INSERT INTO Task (Id,Nome) VALUES (seqTasks.nextval,'"+task+"')")
        connection.commit()
    except cx_Oracle.DatabaseError:
        print("repeated task")
    else:
        print("Task created successfully")


def list_tasks(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT Nome from Task")
    linha = cursor.fetchone()

    if not linha:
        return print("There are not registered tasks")

    while linha:
        print(f" {linha[0]}")
        linha = cursor.fetchone()


def delete_task(connection):
    cursor = connection.cursor()
    task = input("\nTask's name: ")

    cursor.execute("SELECT Id FROM Task WHERE Nome='"+task+"'")
    connection.commit()

    linha = cursor.fetchone()
    if not linha:
        print("Non-existent task")
    else:
        cursor.execute("DELETE FROM Task WHERE Nome='"+task+"'")
        connection.commit()
        print("task removed successfully")


def application_tasks():
    print("Your's Tasks APP")

    server = 'localhost/xe'
    user = 'SYSTEM'
    password = 'gustavo'

    try:
        connection = cx_Oracle.connect(
            dsn=server, user=user, password=password)
        cursor = connection.cursor()
    except cx_Oracle.DatabaseError:
        return "Erro de conexão com o BD\n"

    try:
        cursor.execute(
            "CREATE SEQUENCE seqTasks START WITH 1 INCREMENT BY 1 MINVALUE 1 MAXVALUE 999 NOCACHE CYCLE")
        connection.commit()
    except cx_Oracle.DatabaseError:
        pass

    try:
        cursor.execute(
            "CREATE TABLE Task (Id NUMBER(3) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL)")
        connection.commit()
    except cx_Oracle.DatabaseError:
        pass

    finish_app = False
    while not finish_app:
        print("\n1) Create Task")
        print("2) List Tasks")
        print("3) Delete Tasks")
        print("0) Finish app")

        try:
            opcao = int(input("Digite sua opção: "))
        except ValueError:
            print("Opção inválida\n")
        else:
            if opcao == 1:
                create_task(connection)
            elif opcao == 2:
                list_tasks(connection)
            elif opcao == 3:
                delete_task(connection)
            elif opcao == 0:
                finish_app = True
            else:
                print("Opção inválida")


application_tasks()
