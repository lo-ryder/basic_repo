def cointoss():
    heads=0
    tails=0
    toss = '?'
    for indx in range(1,5001):
        import random
        randomNUM = random.random()
        toss = round(randomNUM)
        if toss == 0:
            toss = 'heads'
            heads= heads + 1
            #print 'heads =',heads
        else:
            toss = 'tails'
            tails = tails + 1
            #print 'tails', tails
        #return indx, toss, heads, tails
        #print indx
        print "Attempt #{}: Throwing a coin... It's a {}(s) there are {} heads and {} tail(s) so far!".format(indx, toss, heads, tails)
print cointoss()

num = 1,2,3
print
