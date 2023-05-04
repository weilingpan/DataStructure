'''Question Number: 15. 3Sum[Medium]
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    
    Notice that the solution set must not contain duplicate triplets.
'''


# nums = [-1,0,1,2,-1,-4]
# target = 0
# #Output: [[-1,-1,2],[-1,0,1]]

# for i in range(len(nums)-1):
#     temp = nums[i:i+2]
#     print(temp,target-sum(temp))

# def add_one(num):
#     num = num +1
# ele = 10
# add_one(num=ele)
# print(ele)

# def add_one(num):
#     num[0] = num[0] + 1
# ele = [10]
# add_one(num=ele)
# print(ele[0])

# def add_one(*num):
#     num = num[0] + 1
# ele = 10
# add_one(ele)
# print(ele)

def my_op(foo1):
    print(2)
    foo1()
    print(3)

@my_op
def my_render():
    print(1)