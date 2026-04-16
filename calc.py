a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

sign = input("Enter operation (+, -, *, /): ")
o = sign.strip()

if o == "+":
  print(a, "+", b, "=",(a+b))
elif o == "-":
  print(a, "-", b, "=",(a-b))
elif o == "*":
  print(a, "*", b, "=",(a*b))
elif o == "/":
  print(a, "/", b, "=",(a/b))
else:
  print("Wrong Input!!")
  
