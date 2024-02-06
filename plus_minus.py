arr = [1, 1, 0, -1, -1]
n =5
positive_count =  0
negative_count = 0
zero_count = 0

for data in arr:
    if(data>0):
        positive_count +=1
    elif(data == 0):
        zero_count+=1
    else:
       negative_count+=1

print("{:.6f}".format(positive_count/n)) 
print("{:.6f}".format(negative_count/n)) 
print("{:.6f}".format(zero_count/n)) 
        