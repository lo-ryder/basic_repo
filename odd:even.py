#prints a string to describe each number as odd or even
# def oddANDeven():
#     for num in range(1,2001):
#         if num%2 == 0:
#             des = 'even'
#             print 'Number is {}. This is an {} number.'.format(num, des)
#         else:
#             des = 'odd'
#             print 'Number is {}. This is an {} number.'.format(num, des)
# oddANDeven()

#this function multiplies the list by a submitted number
# def multiplyList(bigList, multiplier):
#     for num in range(len(bigList)):
#       bigList[num] =  bigList[num]* multiplier
#     return bigList
# print multiplyList([2,4,10,16],5)

#this function prints a list within a list set by input 
def multiplyList(bigList, multiplier):
    for num in range(len(bigList)):
        bigList[num] =  bigList[num]* multiplier
        yo = bigList[num]
        x =[]
        for indx in range(yo):
            x.append(1)
        bigList[num]=x
    return bigList
print multiplyList([2,1,3],2)
