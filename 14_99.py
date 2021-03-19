# ninty nine problems
# source; https://wiki.python.org/moin/ProblemSets/99%20Prolog%20Problems%20Solutions


def main():
    lst = [1, 2, 3, 4, 7]
    print(dupli(lst))
    return


def dupli(lst: list):
    dupe = []

    for i in range(len(lst)):
        dupe.append(lst[i])
        dupe.append(lst[i])

    return dupe


def dupli_example(L):
    return [x for x in L for i in (1,2)]


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
