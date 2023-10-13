'''
Created on 2023/10/13

@author: t21cs009
'''
import math
#コミットしてみる
def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data.pop(0) #データの先頭要素
    
    left = [i for i in data if i <= pivot]#先頭要素以下の値のリスト
    right = [i for i in data if i > pivot]#先頭要素より大きい値のリスト
    
    left = quick_sort(left)
    right = quick_sort(right)
    
    return left + [pivot] + right


print("Hello, Python world")
a = 10
b = 0.000001
c = 'string'
d = 10; e = 0.000001; f = "string"

print(a, b, c)
print(d, e, f)
for x in {1,2,3}:
    print(x)
    
print(type(math))
print(math)

print(math.pi)

data = [7, 1, 4, 2, 8]
print(quick_sort(data))

