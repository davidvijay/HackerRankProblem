n=3
arr = [1,2,3], [4,5,6], [9,8,9]
left_diagonal = []
right_diagonal = []
dec_val = n
count = 0

for i in range (0, n):
    left_diagonal.append(arr[i][i])


for i in range (0, n):
    dec_val = dec_val-1
    right_diagonal.append(arr[i][dec_val])


left_diagonal_sum = sum(left_diagonal)
right_diagonal_sum = sum(right_diagonal)

if (left_diagonal_sum>right_diagonal_sum):
    difference = left_diagonal_sum - right_diagonal_sum
else:
   difference = right_diagonal_sum - left_diagonal_sum 
   
print(difference)