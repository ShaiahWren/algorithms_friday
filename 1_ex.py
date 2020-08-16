
a = [1, 2, 3, 4]
b = [1, 4, 5, 6]
c = [1, 4, 4, 2]
d = [1, 2, 3, 4, 5]
e = [1, 3, 4, 2]

# print(c)
# c.remove(4)
# print(c)


# make empty dictionary
# populate dict with first list
# check if lists are same lengths

def frequency(x, y):
    one_dict = {}
    two_dict = {}
    for i in x:
        if i not in one_dict:
            one_dict[i] = 1
        else:
            one_dict[i] +=1
    for i in y:
        if i not in two_dict:
            two_dict[i] = 1
        else:
            two_dict[i] +=1
        
    if len(one_dict) == len(two_dict):
        for i in one_dict:
            try:
                if one_dict[i] != two_dict[i]:
                    return False
            except:
                return False
        return True
    return False     

print(frequency(a, c))