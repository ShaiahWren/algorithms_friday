a = "hello"
b = "sprinkle slurps"
c = "car cat cuts crinckles"


def most(x):
    one_dict = {}
    for i in x:
        if i not in one_dict:
            one_dict[i] = 1
        else:
            one_dict[i] += 1
 
   
    return (sorted(one_dict, key=one_dict.get, reverse=True))[0]



print(most(c))