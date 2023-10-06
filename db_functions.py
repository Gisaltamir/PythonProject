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
criminal_escaped= False

def get_countries():
    countries= "SELECT country_name FROM hints order by country_name ASC"
    cursor= connection.cursor()
    cursor.execute(countries)
    result= cursor.fetchall()
    print("\nThe countries are:")
    for row in result:
        print(','.join(row))
    print("\n\n")
    return

def get_detective_name():
    detective = "SELECT detective_name FROM detective_game"
    cursor = connection.cursor()
    cursor.execute(detective)
    result = cursor.fetchone()
    return result

def get_criminal_location():
    sql = "SELECT crime_location FROM detective_game"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def get_player_location():
    sql = "SELECT player_location FROM detective_game"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

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

def random_visit_location(quantity):
    sql = "SELECT country_name FROM hints "
    sql += "ORDER BY RAND() "
    sql += "LIMIT " + quantity
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            s = str(row[0])
            visited_locations.append(s)
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
    criminal_escaped= True
    return

def check_if_win():
    crime_location= get_criminal_location()
    player_location= get_player_location()
    if player_location == crime_location:
        print("You have catched the criminal and save the world. Well done, detective")
        return True
    elif criminal_escaped == True:
        print("The criminals escaped, the world is dying. Maybe in another life, detective")
        return True
    else:
        return False

def check_exist_location(answer):
    answer_check = answer.casefold()
    answer_check = answer.capitalize()
    if answer_check in visited_locations:
        return answer_check
    else:
        print("This country is invalid! Check the countries available in display countries")
        return

def player_name():
    name = input("Enter your name, detective: ")
    sql = (f"insert into detective_game(detective_name) values('{name}');")
    cursor = connection.cursor()
    cursor.execute(sql)
    return name
