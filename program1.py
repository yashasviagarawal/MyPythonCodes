def prime_num():  #function declare
  num = int(input("Enter number to check number is prime or not : "))
  if num > 1: #if number is less than one prime num not exit
      for i in range (2 , num // 2):
        if(num % i) == 0: 
            print(num,"is not a prime number")
            break
      else:
          print(num,"is a prime number")
  else:
        print(num,"is not a prime number")

prime_num()

