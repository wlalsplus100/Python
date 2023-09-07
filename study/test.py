for i in range(5):
    for j in range(8):
        for k in range(4):
            print("-", end="")
        print("+", end="")
    print("")

print("\n")

for i in range(6):
    for j in range(5):
        for k in range(6):
            if k == 2:
                print("+", end="")
            else:
                print("-", end="")
    print("")
