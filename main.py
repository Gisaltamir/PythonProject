import db_functions

print("\nIn a world full of threats, the company 'ContaMega Inc.' has created\na deadly chemical called 'Ricina'.\nThe damage to the environment is too high, so with global law\nenforcement, the R-Code Project is starting in order to\ncatch them, but ContaMega Inc. keeps releasing “Ricina” worldwide\nto destroy the evidence.\n\nRed code alert! We need you, agent!\nThe mission is to stop them and their lethal creation Ricina.\nHurry up! before it's too late for the world...\n\n")

name = db_functions.set_player_name()
id = db_functions.id
db_functions.random_visit_location("4")
db_functions.update_crime_location(db_functions.id, 10)

while True:
    try:
        option= int(input(f"\nSelect one of the following actions, agent {name}:\n1- Explore crime scene.\n2- Display possible countries.\n3- Move to destination.\n4- Close the case.\nYour selection: "))
        if option == 1:
            db_functions.get_hint_by_country(db_functions.visited_locations[db_functions.correct_visited_locations+1])
        elif option == 2:
            countries= db_functions.get_countries()
            print("\nThe countries where we know Ricina could be release are:")
            for country in countries:
                print(country)
        elif option == 3:
            answer= input(f"Enter location, agent {name}:\n")
            location= db_functions.check_exist_location(answer)
            if location:
                db_functions.update_player_location(id, location)
                correct= db_functions.check_if_correct(id, location)
                win= db_functions.check_if_win(id)
                if win:
                    break
        elif option == 4:
            print(f"\nSad to see you leave us agent {name}.\n")
            break
        else:
            print("\nNot a valid number.")
    except:
        print("\n\tTry again.")
