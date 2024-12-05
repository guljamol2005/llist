nums = [(1, 2, 3), (3, 4, 5), (5, 6)]
result = ()
num = []
for i in nums:
    result += i
for i in result:
    if i not in num:
        num.append(i)
print("Takrorlanmagan elementlar:", tuple(num))
