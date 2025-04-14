import psycopg2
from psycopg2.extras import execute_values

conn = psycopg2.connect(
    dbname = "lab10",
    user = "tevos",
    password="3489850",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def insertDataSCV():
    data = [] 

    with open("/Users/tevososepyan/Documents/PythonRep/lab10/phones.csv", "r") as file:
        lines = file.readlines()

    for line in lines[1:]:
        splited = line.split(";")
        datapart = (splited[0], int(splited[1][0:-1]))
        data.append(datapart)

    query = "INSERT INTO phonebook (name, phone) VALUES %s"
    
    execute_values(cur, query, data)
    conn.commit()

    cur.close()
    conn.close()

def insertInConsole():
    inputed = input("Print name and phone to add(John, 437834):")
    value = inputed.split(", ")
    
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (value[0], int(value[1])))
    conn.commit()
    print("The data was inserted!")
    cur.close()
    conn.close()
    
def UpdatePhoneOrName():
    letter = input("Chose what to change Name or Phone(N/P):")
    if letter == "N":
        namechose = input("Enter your previous name(John):")
        namenew = input("Enter youe new name(Alex):")
        cur.execute("UPDATE phonebook SET name=%s WHERE name=%s ", (namenew, namechose))
        conn.commit()
        cur.close()
        conn.close()
    if letter == "P":
        namechose = input("Enter your previous phone(11111000):")
        namenew = input("Enter your new phone(983499):")
        cur.execute("UPDATE phonebook SET phone=%s WHERE phone=%s ", (namenew, namechose))
        conn.commit()
        cur.close()
        conn.close()
    
def QueryWithFilters():
    filter = input("Print your name filter or phone filter(A.../8...)")
    if filter[0].isdigit():
        digit = filter[0]
        cur.execute(f"SELECT * FROM phonebook WHERE phone LIKE '3%';")
        print(cur.fetchall())
        cur.close()
        conn.close()

    if filter[0].isalpha():
        letter = filter[0]
        cur.execute(f"SELECT * FROM phonebook WHERE name LIKE '{letter}%';")
        print(cur.fetchall())
        cur.close()
        conn.close()
def DeleteData():
    print()
    
QueryWithFilters()


