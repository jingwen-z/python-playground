stream = ['a|b|c,d,e', 'h|i|j,h,c', 'o|p|q,d,s']

def tag_counts(stream):
    counts_dict = {}
    for string in stream:
        m, v, tags = string.split('|')
        t1, t2, t3 = tags.split(',')
        if not t1 in counts_dict:
            counts_dict[t1] = 1
        elif t1 in counts_dict:
            counts_dict[t1] += 1
        if not t2 in counts_dict:
            counts_dict[t2] = 1
        elif t2 in counts_dict:
            counts_dict[t2] += 1
        if not t3 in counts_dict:
            counts_dict[t3] = 1
        elif t3 in counts_dict:
            counts_dict[t3] += 1

    return counts_dict

print(tag_counts(stream))