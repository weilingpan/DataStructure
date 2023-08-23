'''
    觀念: 不可變物件(Immutable objects)
    定義: 
        - 該物件所指向的記憶體中的值不能被改變。
        - 當改變某個變數的值時，會把原來的值複製一份後再存到新的地址，變數再指向這個新的地址。
    Python中的不可變物件: int, float, bool, str, tuple, unicode
'''

# int 範例
print(f'===== int 範例 =====')
var1 = 1        
print(id(var1), var1)  #id(var1)=1396123238640 值是1，讓var1這個變數參考到了1這個物件
var2 = 1        
print(id(var2), var2)  #id(var2)=1396123238640 值是1
var3 = var1 + 0 
print(id(var3), var3)  #id(var3)=1396123238640 值是1

var4 = var1 + 1 
print(id(var4), var4)  #id(var4)=1396123238672 因值被改變了，值是2
var4 += 1       
print(id(var4), var4)  #id(var4)=1396123238704 因值被改變了，值是3

var4 += 0       
print(id(var4), var4)  #id(var4)=1396123238704 值是3
var4 -= 2       
print(id(var4), var4)  #id(var4)=1396123238640 值是1


def function(myvar):
    myvar += 1
    print(id(myvar), myvar) #2929487249968 11

myvar = 10
print(id(myvar), myvar)     #2929487249936 10
function(myvar)
print(id(myvar), myvar)     #2929487249936 10


# str 範例
# print(f'===== str 範例 =====')
# keyword_list = ["Hello", "World", "Regina"]
 
# content = ""
# print(id(content)) #1396123271216
# for keyword in keyword_list:
#     content += keyword + " "
#     print(id(content), content)
#     # 1893704727600 Hello
#     # 1893704727600 Hello World
#     # 1893704730624 Hello World Regina
# print(id(content)) #1893704730624

# keyword_list = ["Hello", "World", "Regina"]
# result = ""
# print(id(result))
# result = " ".join(keyword_list)
# print(id(result))



'''
    觀念: 可變物件(Mutable objects)
    定義: 物件被創造出來後其值可以做改變
    Python中的可變物件: list, set, dict
'''

# list 範例
print(f'===== list 範例 =====')

def function2(lst):
    lst.append(4)
    print(id(lst), lst) #2014375564992 [1, 2, 3, 4]

lst1 = [1,2,3]
print(id(lst1), lst1)   #2014375564992 [1, 2, 3]
function2(lst1)
print(id(lst1), lst1)   #2014375564992 [1, 2, 3, 4]


#=================================================

# var1 = 1
# var2 = 1
# var3 = 2
# print(id(var1))
# print(id(var2))
# print(id(var3))
# print(var1 == var2)
# print(var1 is var2)

# x = 10
# y = x
# print(id(x))
# print(id(y))

# x += 0
# print(id(x))

# x += 1
# print(id(x))


# list1 = [1, 2, 3]
# list2 = list1
# list2.append(4)

# print(list1)
# print(list2)