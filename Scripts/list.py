lis = ["Kavana", 123, "Sanjana",456,"Spoorthi",789]
num_lis = []
str_lis = []
for i in lis:
    if isinstance(i, int) or isinstance(i, float):
        num_lis.append(i)
    elif isinstance(i, str):
        str_lis.append(i)
    else:
        pass
print(num_lis,str_lis)

