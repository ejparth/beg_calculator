

def multiply(n1,n2):
  return n1*n2

def add(n1,n2):
  return n1+n2

def div(n1,n2):
  return n1/n2

def sub(n1,n2):
  return  n1-n2

operations = {
  "+": add,
  "/": div,
  "*": multiply,
  "-": sub,
}

first_number = int(input("Tell me the first number"))

for operator in operations:
  print(operator)

operator = input("What operation you want from the list?")

second_number = int(input("Tell me the second number"))

operation_functon = operations[operator]

number = operation_functon(first_number,second_number)

print (f"first number {first_number} and second number{second_number} and final output is {number}")
