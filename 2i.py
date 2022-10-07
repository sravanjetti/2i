from collections import defaultdict
 
 
def default_val():
    return 0
 
 
# dict : maintain count of each element. with default value of key is 0
mydict = defaultdict(default_val)
 
# LIST
l = [1, 22, 99, 22, 6, 35, 5, 35, 7, 8]
 
for i in l:
    # if the element already present in the array, remove the element.
    if mydict[i] == 1:
        l.remove(i)
    # If the elements appears first time keep it count as 1
    else:
        mydict[i] = 1
 
# printing the final array
print(l)
