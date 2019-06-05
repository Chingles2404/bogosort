import random

def bogosort():
    unsorted = input("Please input your list in the format \"1, 2, 3\"\n").split(", ")
    compare = sorted(unsorted)
    counter = 1
    print(compare, unsorted)
    while compare != unsorted:
        print("Round " + str(counter))
        temp = []
        while len(unsorted) > 0:
            position = random.randint(0, len(unsorted) - 1)
            temp.append(unsorted[position])
            unsorted.pop(position)
        unsorted = temp
        counter += 1
        print(unsorted)

bogosort()
