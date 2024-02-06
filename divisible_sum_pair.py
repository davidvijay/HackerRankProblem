ar = [1, 3, 2, 6, 1, 2]
k = 3
count=0
for i in range(0, len(ar)):
    for j in range(i, len(ar)-1):
        if(ar[i]+ar[j+1])%k==0:
            count+=1
print(count)