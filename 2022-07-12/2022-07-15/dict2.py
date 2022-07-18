keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
l=len(keys)
res_dict={}
for i in range(l):
    res_dict.update({keys[i]:values[i]})
print(res_dict)
    