import mysql.connector
import json


def connectionDB():
    cnx = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        database='c115'
    )

    cursor = cnx.cursor()
    query = "SELECT * FROM questions"
    cursor.execute(query)

    data = []
    for row in cursor:
        data.append({
            'question': row[1],
            'a': row[2],
            'b': row[3],
            'c': row[4],
            'd': row[5],
            'answer': row[6]
        })

    cursor.close()
    cnx.close()
    return json.dumps(data)
