def difficulty_selector():
    while True:
        try:
            option = int(input("Select difficulty:\n[1]Easy\n[2]Medium\n[3]Hard\n"))
            if option == 1:
                return 50,10,1
            elif option == 2:
                return 100,7,2
            elif option == 3:
                return 200,5,3
            else:
                print("Input must be between 1-3")
        except ValueError:
            print("Input must be an int")
