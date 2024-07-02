
# *Task - 1
list_1=[-4,-16,0,1,4,5,9,121,16,25,36,49,64,81,100]
def myfunc_1(list):
    # 1_Yol
    answer= [ i for i in list if( (i > 0) and ( i ** 0.5).is_integer()) ]
    # answer= [ i for i in list if( (i > 0) and pow(i,1/2).is_integer()) ]
    answer.sort()
    return answer

    # 2_Yol
      # result=[]
      # for i in list:
      #    if i>0 and pow(i,1/2).is_integer():
            
      #        result.append(i)
      # result.sort()
      # return result


# print(myfunc_1(list_1))



# * Task - 2
list_2= [-1,1,2,2,6,7,7,'say']
def my_func_2(list):
  return [ i for i in list if( list.count(i) == 1) ]   


# print(my_func_2(list_2))



# *Task - 3
list_3=[2,4,6,10]
def my_func_3(list):
  result = 1
  #  input : 15 -> 1*5=5
  # for i in input("eded daxil edin:"):
  #    result*=int(i)

  # input:[2,4,6,10]-> 2*4*6*10 = 480
  for i in list:
      result *= i

  return result


# print(my_func_3(list_3))



# * Task - 4
def my_func_4():
  eded=int(input("eded daxil edin:"))
  return [ i for i in range(1,eded+1) if (eded % i == 0) ]

# print(my_func_4())



# * Task - 5
list_5=["yanvar","fevral","mart","aprel","may","iyun","iyul","avqust","sentyabr","oktyabr"]

def my_func_5(list):
  return {x:len(x) for x in list}


# print(my_func_5(list_5))



# * Task - 6
list_6 = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
def my_func_6(list):
# 1 yol
 return([ i.split(" ")[0].lower() for i in list])

# 2 yol
#  return([ i[:i.find(" ")].lower() for i in list])


# print(my_func_6(list_6))



# * Task - 7
nums1 = [1, 2, 4, 8, 6]
nums2 = [4, 5, 6, 1, 2]

def my_func_7(nums_1,nums_2):

#  1_Yol
 return [ (nums_1[i]+nums_2[i])/2 for i in range(len(nums_1))]

#  2_Yol
  # result=[]
  # for i in range(len(nums_1)):
  #   result.append((nums_1[i] + nums_2[i])/2)

  # return result

# print(my_func_7(nums1,nums2))
