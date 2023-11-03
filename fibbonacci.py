def fibonacci(n):
     a,b=0,1
     count=0
     while count<n:
        print(a, end=" ")
        a,b=b,a+b
        count=count+1
n=int(input("Enter the no of terms: "))
if n<=0:
    print("Enter positive integer: ")
else:
     print("fibonacci series: ")
     fibonacci(n)
