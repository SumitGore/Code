def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 ==0:
            print("Fizz")
        elif i % 5 ==0:
            print("Buzz") 
        else:
            print(i)
#Take input from the user            
n = int(input("enter the upper limit: "))
fizzBuzz(n)