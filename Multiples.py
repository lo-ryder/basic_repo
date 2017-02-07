# Part1 printing odd nums from 1 to 1000
# for num in range(1001):
#     if num%2 !=0:
#         print num
#     else:
#         continue

# Part2 printing odd nums from 5 to 1,000,000
# for num in range(5,1000001):
#     if num%5==0:
#         print num
#     else:
#         continue

#Sum List this function adds up all the values in a list
# def SumList(a):
#     sum = 0
#     for things in range(0,len(a),1):
#         sum += a[things]
#     return sum
# print SumList([1,2,5,10,255,3])

#AvgList averages all the items in the list even if they dont divide evenly
def AvgList(a):
    avg = 0
    for things in range(len(a)):
        avg = avg + float(a[things])/len(a)
    return float(avg)
print AvgList([1,2,5,10,255,3])
