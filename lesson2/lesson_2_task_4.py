def fizz_buzz(n):
    for s in range (1, n+1):
        if s % 3 == 0 and s % 5 == 0: print ("FizzBuzz")
        elif s % 3 == 0: print ("Fizz")
        elif s % 5 == 0: print ("Buzz")
        else: print (s)

fizz_buzz(17)