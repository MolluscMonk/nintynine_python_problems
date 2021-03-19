# ninty nine problems
# source; https://wiki.python.org/moin/ProblemSets/99%20Prolog%20Problems%20Solutions


def main():
    lst = [1, 2, 3, 4, 7]
    N = 3
    print(dupli(lst, N))
    return


def dupli(lst: list, N: int):
    dupe = []

    for i in range(len(lst)):
        for j in range(N):
            dupe.append(lst[i])

    return dupe


def dupli_example(L):
    return [x for x in L for i in (1, 2)]


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
