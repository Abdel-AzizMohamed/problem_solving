###### Solution 1


def reverse_slice(s):
    result = []
    rev = s[::-1]
    length = len(rev)

    for i in range(length):
        result.append(rev[i:])

    return result


###### Solution 2


def reverse_slice(s):
    return [s[::-1][i:] for i in range(len(s))]


print(reverse_slice("abcde"))
