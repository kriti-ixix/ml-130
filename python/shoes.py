shoes = {1:10, 2:20, 3:0, 4:5, 5:20}

while True:
    choice = int(input("Enter a size: "))

    if choice == 100:
        break
    else:
        if shoes[choice] == 0:
            print("Sorry we are out of stock")
        else:
            print("Giving you a {} size shoe".format(choice))
            shoes[choice] -= 1

    print(shoes)