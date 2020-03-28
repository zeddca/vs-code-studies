#全排列调用itertools.permutations()
def permutation(s):
    if len(s) == 0 or len(s) == 1:
       return [s]
    re = []
    for i in s:
       temp_list = s[:] 
       temp_list.remove(i)
       temp = permutation(temp_list) 
       for j in temp:  
           j[0:0] = [i]  
           re.append(j)
    return re