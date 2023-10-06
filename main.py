import db_functions

db_functions.random_visit_location("4")
db_functions.update_crime_location(10)
print("\nIn a world under threat from the secret group 'ContaMega Inc.' they've created a deadly chemical called 'Ricina' for profit.\nGlobal law enforcement was close to catchingth e them, but ContaMega Inc. plans to release 'Ricina' worldwide to destroy evidence.\nAs a detective, it's your mission to stop them and their lethal creation 'Ricina' before it's too late for the world!\n\n")
name= db_functions.player_name()
while True:
    try:
        option= int(input(f"\nSelect one of the following actions, agent {name}:\n1- Explore crime scene.\n2- Display possible countries.\n3- Move to destination.\n4- Close the case.\nYour selection: "))
        if option == 1:
            db_functions.get_hint_by_country(db_functions.visited_locations[db_functions.correct_visited_locations])
        elif option == 2:
            db_functions.get_countries()
        elif option == 3:
            answer= input(f"Enter location, agent {name}:\n")
            location= db_functions.check_exist_location(answer)
            if location:
                correct= db_functions.check_if_correct(location)
                if correct:
                    db_functions.check_if_win()
        elif option == 4:
            print(f"\nSad to see you leave us, agent {name}.\n")
            break
    except:
        print(f"\n\nYour only choice is to select the numbers from 1 to 4, detective {name}.\n\n")
