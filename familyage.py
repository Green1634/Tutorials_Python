print("enter your firstborn age")
firstborn = input ()

print("enter secondborn age")
secondborn = input ()

print("enter thirdborn age")
thirdborn = input ()

print("enter fourthborn age")
fourthborn = input ()

print("enter fifthborn age")
fifthborn = input ()

total_age = (int(firstborn) + int(secondborn) + int(thirdborn) + int(fourthborn) + int(fifthborn))

Average = total_age/5

MaximumAge = max(int(firstborn), int(secondborn), int(thirdborn), int(fourthborn), int(fifthborn))

MinimumAge = min(int(firstborn), int(secondborn), int(thirdborn), int(fourthborn), int(fifthborn))

print(f"Total Age is: {total_age}, Maximum is: {MaximumAge}, Minimum is: {MinimumAge},")