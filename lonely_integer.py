from collections import Counter

my_list = [1,2,3,4,3,2,1]

counts = Counter(my_list)
for i,j in counts:
    if(j==1):
      print(i)