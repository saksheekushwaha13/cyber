print("True if the array contains a 3 next to a 3 somewhere")


def has_33(list):
    x = int(len(list) - 1)
    for i in range(x):
        if ((list[i] == 3) and (list[i + 1] == 3)):
            return True
        else:
            return False


list = [3, 3, 1]
has_33(list)