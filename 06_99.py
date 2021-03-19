# ninty nine problems
# source; https://wiki.python.org/moin/ProblemSets/99%20Prolog%20Problems%20Solutions


# starting with 6
# Flaten a nested list structure

l1 = [1, [2, 3]]
l2 = [[1, 2], 3]
l3 = [1, 2, [3, [4, 5, [6], 7], 8], 9]


def main():

    done = False
    index = 0
    flat_list = []
    nest_list = [l1, l2, l3]
    for lst in nest_list:
        while not done:
            if type(lst[index]) is list:
                
                print(lst[index])

            else:
                flat_list.append(lst[index])
                print(flat_list)
            index += 1



    return


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
