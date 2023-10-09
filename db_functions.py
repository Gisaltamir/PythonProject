import mysql.connector
import random

connection = mysql.connector.connect(
    host= "127.0.0.1",
    port= 3306,
    database= "crime_game",
    user= "root",
    password= "",
    autocommit= True
)

name= ""
visited_locations= ["Base", ]
correct_visited_locations= 0
criminal_escaped= False
id = 0


def get_countries():
    countries= "SELECT country_name FROM hints order by country_name ASC"
    cursor= connection.cursor()
    cursor.execute(countries)
    result= cursor.fetchall()
    countries= []
    for row in result:
        countries.append(row[0])
    return countries

def get_detective_name(id):
    detective = f"SELECT detective_name FROM detective_game where id = {id}"
    cursor = connection.cursor()
    cursor.execute(detective)
    result = cursor.fetchone()
    return result

def get_criminal_location(id):
    sql = f"SELECT crime_location FROM detective_game where id = {id}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[0]

def get_player_location(id):
    sql = f"SELECT player_location FROM detective_game where id = {id}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def get_hint_by_country(country):
    sql = f"SELECT hint FROM hints where country_name = '{country}'"
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

def update_player_location(id, location):
    sql = f"UPDATE detective_game SET player_location = '{location}' where id = {id}"
    cursor = connection.cursor()
    cursor.execute(sql)
    countries = cursor.fetchall()
    return
    
def update_crime_location(id, number):
    global criminal_escaped
    global visited_locations
    sql = ("select country_name from hints;")
    cursor = connection.cursor()
    cursor.execute(sql)
    countries = cursor.fetchall()
    countries = [country[0] for country in countries]
    while len(visited_locations) < number:
        ranNum = random.randrange(0, number)
        if countries[ranNum] not in visited_locations:
            visited_locations.append(countries[ranNum])
            updateQuery = (f"UPDATE detective_game SET crime_location = '{countries[ranNum]}' WHERE id = {id}")
            cursor.execute(updateQuery)
            break
    if len(visited_locations) == number:
        criminal_escaped = True
        return

def check_if_correct(id, location):
    global correct_visited_locations
    if location == visited_locations[correct_visited_locations+1]:
        correct_visited_locations += 1
        print(f"\nYou solved the case and went to the correct country!\nYou are now in {location}. Good job!")
        return True
    else:
        update_crime_location(id, 10)
        print(f"\nYour answer is wrong. One more box of Ricina is dropped by ContaMega.\nYou are now in {location}.")
        return False

def check_if_win(id):
    global criminal_escaped
    global visited_locations
    crime_location= get_criminal_location(id)
    if visited_locations[correct_visited_locations] == crime_location:
        print(f"\nYou have catched the criminal and save the world. Well done, detective {name}")
        return True
    elif criminal_escaped == True:
        print("\nThe criminals escaped, the world is dying. Maybe in another life, detective")
        return True
    else:
        return None

def check_exist_location(answer):
    answer_check = answer.casefold()
    answer_check = answer.title()
    countries= get_countries()
    if answer_check in countries:
        return answer_check
    else:
        print(f"\nThis country is invalid! Check the countries available in:\n\t'Option 2: Display possible countries'")
        return

def set_player_name():
    global name
    global id
    name = input("Enter your name, detective: ")
    sql = (f"insert into detective_game(detective_name) values('{name}');")
    cursor = connection.cursor()
    cursor.execute(sql)
    id = cursor.lastrowid
    return name
