x = []
num1 = 0
incr = 0


while num1 in range (100):
    num1 = int(raw_input ("number: "))
    x.append(num1)
    print "list is: %s" % x
    if num1 == 100:
        print "This is the end."
    elif num1 >= 0:
        num1 =+ 1
        incr = incr + num1
        print "total number of values: %s" % incr

#adding user input values into list.
#a variable shows incrementing values, which is saved.
#incremented values are printed which shows total number of values in list.
#if user hits key value, 100, the list ends. 
