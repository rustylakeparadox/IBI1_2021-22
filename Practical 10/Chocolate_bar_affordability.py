def caculate_bar():
   x = int(input('the total money is '))
   y = int(input('the price is '))
   left_over = x % y
   number = (x-left_over)/y
   return left_over, number

#given an example
caculate_bar()
#input x = 100, y = 7
## (2,14.0)