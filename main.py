from random import randint

"""
    multiplication quiz app
"""

print("-" * 50)
print("\t\tWELCOME..")
print("-" * 50, "\n")


def multi(i, j, r):
    if r != "-1":
        result = str(i * j)
        if result == r:
            print("\t\t***** Correct *****")
        else:
            print("\t!!! Wrong it was %s " % result)
    else:

        select()


def start(rng_1, rng_2):
    if rng_1 > 10:
        x = 10
    else:
        x = 5
    for i in range(0, x):
        for j in range(0, x):
            sayi_1 = randint(rng_1, rng_2)
            sayi_2 = randint(rng_1, rng_2)
            print("_" * 50, "\n")
            print("\t%d x %d ? (exit = -1)" % (sayi_1, sayi_2))
            sonuc = input("result >> ")
            multi(sayi_1, sayi_2, sonuc)

            if i == 4 and j == 4:
                print("\n *-- This level and you can jump to next level --*\n")
                select()


def select():
    print(" Please choice level (exit = -1) ?\n")
    print("  1 - Easy ")
    print("  2 - Medium ")
    print("  3 - Hard")
    print("  4 - Very Hard\n")

    svy = input(" >> ")

    if svy == "1":
        start(1, 6)

    elif svy == "2":
        start(6, 12)

    elif svy == "3":
        start(12, 25)

    elif svy == "4":
        start(25, 100)

    else:
        exit(0)


if __name__ == '__main__':
    select()