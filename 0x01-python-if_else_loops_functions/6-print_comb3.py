#!/usr/bin/python3
for k in range(100):
    if int(k / 10) != k % 10 and int(k / 10) < k % 10:
        print("{}{}".format(int(k / 10), k % 10), end="")
        if (k != 89):
            print(", ", end="")
print("")
