##print(len('aaaaa'))
##-------------------------字符的分割与连接-------
s='a,b,b,b,b'
sp=s.split(',')
sp2='-'.join(sp)
print(s)
print(sp)
print(sp2)

#--------------------------递归 hanoi塔----------
def hanoi(n,A,B,C):
	if n==1:
		print(A+'->'+B)
	else:
		hanoi(n-1,A,C,B)
		print(A+'->'+B)
		hanoi(n-1,C,B,A)		
hanoi(2,'A','B','C')

#------------------------list的增删、查找以及判断---------
list1=[1,2,3]
list2=[1,2,3]
list1.append(4)
#将数组作为一个整体加入list
list1.append([4,5,6])
del(list1[1])
print(list1)
#将数组内数逐个加入
list2.extend([4,5,6])
print(list2)
#查找
print(list2.index(4))
#判断为空
lst=[]
if not lst:
    print('Empty')
if len(lst)==0:
    print('Empty')
if not list or len(lst)==0:
    print('Empty')
#遍历list
for i in list2:
    print(i)
for i in range(len(list2)):
    print(list2[i])

#---------------------------tuple （只读）-------------------
tp=(1,2,3,4,5,6)
print(type(tp))
#练习tuple two_sum 找出数组中和为*的所有组合
def two_sum(numbers,target):
    result=[]
    for i in numbers:
        try:
            num_index=numbers.index(target-i)
        except:
            continue
        result.append([i,numbers[num_index]])        
    return result

print(two_sum([1,2,3,4,5,6,7],7))
#上述方法可以实现，但是会有重复 改进后
def two_sum(numbers,target):
    result=[]
    for i in numbers:
        try:
            num_index=numbers.index(target-i)
        except:
            continue
        if num_index>numbers.index(i):
            result.append([i,numbers[num_index]])        
    return result

print(two_sum([1,2,3,4,5,6,7],7))
print(two_sum([1,8,7,2,4,5,6,3],9))

#---------------------------dict 无序的----------------------
d={1:'A',2:'B',3:'C',4:'D'}
print(type(d))
print(d)
#访问元素
print(d[1])
print(len(d))
#判断key是否存在
print('A' in d)
print(1 in d)
#删除
del(d[2])
print(d)
#增加
d[2]='B'
print(d)
#遍历字典
for key in d:
    print(key)
for val in d.items():
    print(val)
for key,val in d.items():
    print(key,val)
keys=d.keys()
print(type(keys))
print(keys)

#---------------------set  无序，无重复元素，有会自动删除----------------------
s1=set([1,2,3,4,5,6])
s2=set([1,2,5,7,8,9])
print(s1)
#判断元素是否存在
print(6 in s1)
print(7 in s1)
#并集
print('并集',s1|s2)
print('并集',s1.union(s2))
#交集
print('交集',s1&s2)
print('交集',s1.intersection(s2))
#差集
print('差集',s1-s2)
print('差集',s1.difference(s2))
#对称差，异或
print('对称差',s1^s2)
print('对称差',s1.symmetric_difference(s2))
#添加
s1.add('a')
s1.update([1,2,8,'b'])
print(s1)
#删除 只能直接指定值
s1.remove(2)
print(s1)
print(len(s1))
# 遍历
for i in s1:
    print(i)
#----------------------------切片[start:end:step] 前闭后开----------------------------
inistr=list(range(9))
print(inistr)
print('切片',inistr[2:5])
print('切片',inistr[2:])
print('切片',inistr[:5])
#负值处理
print('切片',inistr[1:-1]) #1- -2
print('切片',inistr[9:0:-1])#切片 [8, 7, 6, 5, 4, 3, 2, 1]
print('切片',inistr[9::-1])#切片 [8, 7, 6, 5, 4, 3, 2, 1, 0]
print('切片',inistr[::-2])#切片 [8, 6, 4, 2, 0]
