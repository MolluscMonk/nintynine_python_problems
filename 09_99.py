# ninty nine problems
# source; https://wiki.python.org/moin/ProblemSets/99%20Prolog%20Problems%20Solutions

# 9
# Problem 9: Pack consecutive duplicates of list elements into sublists


l1 = [1, 1, 1, 2, 3]
l2 = [1, 2, 3, 3, 3]
l3 = [1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 9, 9, 9]


def main():

    list_list = [l1, l2, l3]
    for lst in list_list:
        fresh_list, dupe_list = remove_dupe(lst)
        print(fresh_list, '\n', dupe_list)

    return


def remove_dupe(lst: list):
    rng = len(lst) - 1
    offset = 0
    dupes = []
    for i in range(rng):
        j = i + 1 - offset
        k = i - offset
        if lst[k] == lst[j]:
            dupe = lst.pop(k)
            dupes.append(dupe)
            offset += 1
    return lst, dupes


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
