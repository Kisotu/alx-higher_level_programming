#!/usr/bin/python3
for i in range(100):
    if x == 99:
        print(i)
    else:
        print("{}".format('0' + str(x) if x < 10 else x), end=", ")
