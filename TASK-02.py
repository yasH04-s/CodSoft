def add(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  return x/y
def square(x,y):
  return x**y
def percent(x,y):
  return (x/y)*100
def logarithm(x,y):
  return log(x,y)

while True:
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Square")
  print("6. Percentage")
  print("7. Log")
  print("8. Exit")

  opt=int(input("enter the option: "))

  if opt>=1 and opt<=8:
    a= float(input("enter the no. : "))
    b= float(input("enter the no. : "))

    if opt == 1:
      print(a,'+',b,'=', add(a,b))

    elif opt == 2:
      print(a,'-',b,'=',subtract(a,b))

    elif opt == 3:
      print(a,'*',b,'=',multiply(a,b))

    elif opt == 4:
      print(a,'/',b,'=',divide(a,b))

    elif opt == 5:
      print(a,'**',b,'=',square(a,b))

    elif opt == 6:
      print(a,'/',b,'*100','=',percent(a,b))

    elif opt == 7:
      if a > 0 and b > 0:
        print('log of', a, 'for base', b, 'is =', log(a, b))
      else:
        print("Invalid input for logarithm")

    elif opt == 8:
      print("Exit",a,b)
      break
  else:
        print("Invalid option. Try again.")

  print("Happy Calculation!")