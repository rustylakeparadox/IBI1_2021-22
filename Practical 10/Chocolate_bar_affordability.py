def caculate_bar():   # create a function
   # input the variable x, y and swift them to strings
   x = int(input('the total money is '))    
   y = int(input('the price is '))
   left_over = x % y          # caculate the left over money
   number = (x-left_over)/y   # caculate number of chocolate bars
   return left_over, number    # return the outcomes

# give an example
caculate_bar()  # call the function
# input x = 100, y = 7
## (2,14.0)
