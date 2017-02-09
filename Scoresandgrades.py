import random
import math
# the random function will return a floating point number,
# that is 0.0 <= random_num < 1.0

# def grader():
#     score = raw_input('Enter your score for test')
#     print score
#     for indx in range (1,10):
#         score = input('Enter your score for test')
#         if score >=60 and score <=69:
#             print 'Your grade is D'
#         elif score >=70 and score<=79:
#             print 'Your grade is C'
#         elif score >=80 and score<=89:
#             print 'Your grade is B'
#         else:
#             print 'Your grade is A'
def score():
    print 'Score and Grades'
    for indx in range(10):
        random_num = int(random.random()*40+60)
        howudid = 'ok'
        if random_num >=60 and random_num <=69:
            howudid = 'D'
        elif random_num >=70 and random_num<=79:
            howudid = 'C'
        elif random_num >=80 and random_num<=89:
            howudid = 'B'
        else:
            howudid = 'A'
        print "Score:",random_num,';', "Your grade is", howudid
    print 'End of the program. Bye!'
print score()
