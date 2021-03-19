# ninty nine problems
# source; https://wiki.python.org/moin/ProblemSets/99%20Prolog%20Problems%20Solutions


# starting with 6
# Flaten a nested list structure

l1 = [1, [2, 3]]
l2 = [[1, 2], 3]
l3 = [1, 2, [3, [4, 5, [6], 7], 8], 9]


def main():

    flat_list = []
    nest_list = [l1, l2, l3]
    for lst in nest_list:
        flat_list = flatten(lst)
        print(flat_list)
    return


def flatten(lst: list):
    done = False
    index = 0
    flat_list = []
    while not done:
        if type(lst[index]) is list:
            flattened = flatten(lst[index])
            for item in flattened:
                flat_list.append(item)
            index += 1
        else:
            flat_list.append(lst[index])
            index += 1
        if len(lst) <= index:
            return flat_list


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
