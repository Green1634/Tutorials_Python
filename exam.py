passedStudent = 0

print("enter first student score")
first = int(input ())

print("enter second student score")
second = int(input ())

print("enter third student score")
third = int(input ())

print("enter fourth student score")
fourth = int(input ())

print("enter fifth student score")
fifth = int(input ())

if first > 69: 
    passedStudent = passedStudent + 1

if second > 69: 
    passedStudent = passedStudent + 1

if third > 69: 
    passedStudent = passedStudent + 1

if fourth > 69: 
    passedStudent = passedStudent + 1

if fifth > 69: 
    passedStudent = passedStudent + 1

print(f"Pass Student is: {passedStudent}")


