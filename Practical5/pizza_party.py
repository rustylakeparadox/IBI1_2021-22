p = 1
# the initial value for p should be 1
n = 0
# the initial value for n should be 1
while p < 64:
# set a loop and make it stop once p reaches 64
  n = n + 1
  # increase n each time 
  p = (n * n + n + 2)/2
  # import the calculation formula of p
  
  print("whis is the" + str(n) + "th(st/rd) time of cutting, the	total	number	of pieces	of	pizza is" + str(p))
# output the outcome