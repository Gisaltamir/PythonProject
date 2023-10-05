import db_functions

name= input("Enter your name, detective: ")

db_functions.random_visit_location("4")
db_functions.update_crime_location()

while True:
    option= int(input("Select one of the following actions:\n1- Explore crime scene.\n2- Display possible countries.\n3- Move to destination.\n4- Close the case.\nYour selection: "))
    if option == 1:
        db_functions.get_hint_by_country(db_functions.visited_locations[db_functions.correct_visited_locations])
    elif option == 2:
        db_functions.display_countries()
    elif option == 3:
        answer= input("Enter location: ")
    elif option == 4:
        print("Bye")
        break
