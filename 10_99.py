# ninty nine problems
# source; https://wiki.python.org/moin/ProblemSets/99%20Prolog%20Problems%20Solutions

# Problem 10: Run-length encoding of a list

l1 = ['a', 'a', 'a', 'b', 'c']
l2 = ['a', 'b', 'c', 'c', 'c']
l3 = ['a', 'b', 'c', 'c', 'd', 'e', 'f', 'f', 'g', 'h', 'i', 'i', 'j', 'j', 'j']


def main():

    list_list = [l1, l2, l3]
    for lst in list_list:
        encoded_list = encode(lst)
        print(lst, '\n', encoded_list)

    return


def encode(lst: list) -> list:
    encoded_list = []

    for i1 in lst:
        count = 0
        for i2 in lst:
            if i1 == i2:
                count += 1
        new_val = str(count) + i1
        if new_val in encoded_list:
            continue
        encoded_list.append(str(count) + i1)

    return encoded_list


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
