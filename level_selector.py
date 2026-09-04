def difficulty_selector():
    print("What level of difficulty would you like to use?\n--Easy(1-50,10 tries)\n--Medium(1-100,7 tries)\n--Hard(1-200,5 tries)")
    while True:
        try:    
            num = int(input())
            break
        except ValueError:
            print("Input must be an integer")

    if num > 0 and num <= 50:
        return "Easy",10,num
    elif num > 50 and num <= 100:
        return "medium",7,num
    elif num > 0 and num <= 200:
        return "Hard",5,num
