def powerset(string):
    res = []
    for i in range(2**len(string)):
        nstring = ""
        for j in range(len(string)):
            if i&(1<<j):
                nstring+=string[j]
        res.append(nstring)
    return res


def generate_all_substring():
    ...