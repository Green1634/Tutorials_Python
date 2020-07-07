
# name = input ()
# print(f"hello, {name}!")

# i = 28
# print(f"i is {i}")

# f = 2.8
# print(f"f is {f}")

# b = False
# print(f"b is {b}")

# n = None
# print(f"n is {n}")


# x = -28

# if x > 0:
#     print("x is positive")

# elif x< 0:
#     print("x is negative")

# else:
#     print("x is zero")

# name = "Ivana"

# coordinates = (10.0, 20.0)

# # names  = ["Alice", "Bob", "Jotham"]

# for i in range(100):
#     print(i)

# names  = ["Alice", "Bob", "Jotham"]
# for name in names:
#     print(names)

# s = set()
# s.add (1)
# s.add (2)
# s.add (2)
# s.add (1)
# print(s)

# ages = {"Green": 26, "Ayo": 31, "Me": 20}
# ages ["Ivana"] = 7
# ages["Ayo"] += 1

# print(ages)

# def square(x):
#     return x * x

# for i in range(10):
#     print("{} squard is")

print("enter intial initial velocity") 
initial_velocity = input ()

print("enter final velocity")
final_velocity = input()

print("enter time taken")
time_taken = input()

acceleration = (int(final_velocity) - int(initial_velocity)) /int(time_taken)

print(f"Initial velocity is: {initial_velocity} m/s, final velocity is: {final_velocity} m/s, time taken is: {time_taken} s, Acceleration is: {acceleration} m/s^2,")