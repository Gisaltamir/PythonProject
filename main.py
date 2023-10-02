name= input("Enter your name, detective: ")



while True:
    option= int(input("Select one of the following actions:\n1- Explore crime scene.\n2- Display possible countries.\n3- Move to destination.\n4- Close the case.\nYour selection: "))
    if option == 1:
        print("HINT")
    elif option == 2:
        print("Countries: ")
    elif option == 3:
        answer= input("Enter location: ")
    elif option == 4:
        print("Bye")
        break
