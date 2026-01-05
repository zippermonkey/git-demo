#数据结构练习
my_list=[3,1,4,2]
my_list.append(5)
my_list.pop(1)
my_list.sort()
print("列表操作结果： ", my_list)

my_dict={"name":"test","age":25}
my_dict["gender"]="male"
print("字典取值：",my_dict.get("addr","default"))
print("字典键值对：",list(my_dict.items()))

my_set1={1,2,3,3,4}
my_set2={3,4,5,6}
print(my_set1)
print(my_set1&my_set2)
print(my_set1|my_set2)

my_tuple=(10,20,30)
a,b,c=my_tuple
print(a, b, c)
