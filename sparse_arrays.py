#link: https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

strings = ["aba", "baba", "aba", "xzxb"]
queries = ["aba", "xzxb", "ab"]


result = []

for i in queries:
    count = 0
    
    for j in strings:
        if (i==j):
            count+=1
    result.append(count)
print(result)
        