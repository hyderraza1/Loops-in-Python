num = int(input("Enter number to be checked: "))
flag = True


if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            flag = False
            break

if flag:
    print(num, "It's a prime number.")
else:
    print(num, "It's not a prime number.")
      
        
