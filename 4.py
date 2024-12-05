num =[(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d')]
result =[]
for i in num:
    if len(i)!=0:
        result.append(i)
print(result)