nums = [1, 'a', 1, 'b', 10, 'b']
result =[]
for i in nums:
    if i not in result:  
        result.append(i)
print(result)



