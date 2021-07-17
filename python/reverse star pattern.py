# for row in range(5, 0, -1):
#     for col in range(1, row+1):
#         print("* ", end='')
#     print("")

stars = 5

for row in range(1, 6):
    for col in range(1, stars+1):
        print("* ", end='')
    print("")
    stars -= 1
