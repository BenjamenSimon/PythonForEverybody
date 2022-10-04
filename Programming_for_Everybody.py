
## Assignment 1

print("Assignment 1: Installing Python Screenshots")

## Assignment 2

print("hello world")


## Exercise 2.2

name = input("Enter your name")
print("Hello", name)


## Exercise 2.3

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

pay = float(hrs) * float(rate)

print('Pay:', pay)


## Exercise 3.1

hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
rate = float(rate)

if h > 40 :
    rem = h-40
    pay = rate*40 + rate*rem*1.5
else :
    pay = rate * h

print(pay)


## Exercise 3.3

score = input("Enter Score: ")
score = float(score)

if score > 1.0 :
    print('Error: Please enter a value between 0.0 and 1.0')
elif score < 0.0 :
    print('Error: Please enter a value between 0.0 and 1.0')
elif score >= 0.9 :
    print('A')
elif score >= 0.8 :
    print('B')
elif score >= 0.7 :
    print('C')
elif score >= 0.6 :
    print('D')
else :
    print('F')


## Exercise 4.6

def computepay(h, r):

    if h > 40 :
        rem = h-40
        pay = r*40 + r*rem*1.5
    else :
        pay = r * h

    return(pay)

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

p = computepay(hrs, rate)

print("Pay", p)


## Exercise 5.2

largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    try :
        num = int(num)
    except :
        print('Invalid input')
        continue

    if largest is None :
        largest = num
        smallest = num

    if largest < num :
        largest = num

    if smallest > num :
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
