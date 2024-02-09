arr = [1,2,3,4,5]
result = []


for i in range(0, len(arr)):
    temp = i
    sum_val = 0
    
    for j in range(0, len(arr)):
        if (j==temp):
            continue
        else:
            sum_val+=arr[j]
    result.append(sum_val)       
print(min(result), max(result) )
