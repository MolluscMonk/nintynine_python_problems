# ninty nine problems
# source; https://wiki.python.org/moin/ProblemSets/99%20Prolog%20Problems%20Solutions

# Problem 13: Run-length encoding of a list (direct solution)
# I am not sure how this is different then problem 11
from itertools import groupby


l1 = ['a', 'a', 'a', 'b', 'c']
l2 = ['a', 'b', 'c', 'c', 'c']
l3 = ['a', 'b', 'c', 'c', 'd', 'e', 'f', 'f', 'g', 'h', 'i', 'i', 'j', 'j', 'j']


def main():

    list_list = [l1, l2, l3]
    for lst in list_list:
        # encoded_list = encode(lst)
        # print(lst, '\n', encoded_list)
        # print('%$#@@')
        # decoded_list = decode(encoded_list)
        # print(lst, '\n', decoded_list)
        print(encode_modified(lst))
        print(decode_example(encode_example(lst)))
        print('xxx')
        # print(encode_direct(lst))
        print('xxx')

    return


# def encode_direct(alist):
#     def aux(k, g):
#         l = len(list(g))
#         if l > 1: return [l, k]
#         else: return k
#     return [aux(key, group) for key, group in groupby(alist)]


def encode_example(alist):
    return [[len(list(group)), key] for key, group in groupby(alist)]


def decode_example(alist):
    def aux(g):
        if isinstance(g, list): return [(g[1], range(g[0]))]
        else: return [(g, [0])]
    return [x for g in alist for x, R in aux(g) for i in R]


def encode_modified(alist):
    def aux(lg):
        if len(lg) > 1: return [len(lg), lg[0]]
        else: return lg[0]
    return [aux(list(group)) for key, group in groupby(alist)]


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
        if count == 1:
            encoded_list.append(str(i1))
        else:
            encoded_list.append(str(count) + i1)

    return encoded_list


def decode(lst: list) -> list:
    decoded_list = []

    for item in lst:
        if len(item) == 1:
            decoded_list.append(item)
        else:
            for i in range(len(item) + 1):
                decoded_list.append(item[1])
    return decoded_list




    return



if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
