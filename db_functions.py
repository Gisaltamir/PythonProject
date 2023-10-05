import mysql.connector
import random

connection = mysql.connector.connect(
    host= "127.0.0.1",
    port= 3306,
    database= "crime_game",
    user= "root",
    password= "123456",
    autocommit= True
)

visited_locations= []
correct_visited_locations= 0
def random_visit_location(quantity):
    sql = "SELECT country_name FROM hints "
    sql += "ORDER BY RAND() "
    sql += "LIMIT " + quantity
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    list= []
    if cursor.rowcount > 0:
        for row in result:
            s = str(row[0])
            visited_locations.append(s)
    return

def get_hint_by_country(country):
    sql = "SELECT hint FROM hints where country_name = '" + country + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount > 0:
        for row in result:
            s = str(row)
            decoded_string = bytes(s, 'utf-8').decode('unicode-escape')
            print(decoded_string)
    return


def update_crime_location(number):
    fetchQuery = ("select country_name from hints;")
    cursor = connection.cursor()
    cursor.execute(fetchQuery)
    countries = cursor.fetchall()
    countries = [country[0] for country in countries]
    while len(visited_locations) != number:
        ranNum = random.randrange(0, number)
        if countries[ranNum] not in visited_locations:
            visited_locations.append(countries[ranNum])
            updateQuery = (f"insert into detective_game(crime_location) values('{countries[ranNum]}');")
            cursor.execute(updateQuery)
            break
    return

def display_countries():
    countries= "SELECT country_name FROM hints"
    cursor= connection.cursor()
    cursor.execute(countries)
    result= cursor.fetchall()
    print("\nThe countries are:")
    for row in result:
        print(','.join(row))
    print("\n\n")
    return

