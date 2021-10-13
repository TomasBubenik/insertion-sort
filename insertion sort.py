val = [4,6,1,7,9,2]
def insertion_sort(val):
    for i in range(1,len(val)):
        key = val[i]
        j = i-1
        while j>=0 and key < val[j]  :
           val[j+1] = val[j]
           j -= 1
        val[j+1] = key



insertion_sort(val)
print(val)
