a = "pie"
b = "eip"
c = "pies"
d = "pwe"

def anagram(x, y):
    one_dict = {}
    two_dict = {}
    for i in x:
        if i not in one_dict:
            one_dict[i] = 1
        else:
            one_dict += 1
    for i in y:
        if i not in two_dict:
            two_dict[i] = 1
        else:
            two_dict[i] += 1
    if len(one_dict) == len(two_dict):
        for i in one_dict:
            try:
                if one_dict[i] != two_dict[i]:
                    return False
            except:
                return False
        return True

    return False

print(anagram(a, a))