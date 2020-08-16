import math
import pdb

a = [1, 2, 3, 4]
b = [1, 4, 9, 16]
c = [1, 4, 5, 6]
d = [1, 4, 4, 2]
e = [1, 16, 9, 4]
f = [1, 2, 3, 4, 5]

def powers(x, y):
    one_dict = {}
    two_dict = {}

    for i in x:
        if i**2 not in one_dict:
            one_dict[i**2] = i
        else:
            pass
    
    
    for i in y:
        if i not in two_dict:
            two_dict[i] = math.sqrt(i)
        else:
            pass
    
    if len(one_dict.keys()) == len(two_dict.keys()):
        for i in one_dict:
            try:   
                if one_dict[i] != two_dict[i]:
                    return False
            except:
                return False
        return True
    
    else:
        return False
    

print(powers(a, b))