#a = 5
#print(a)

#b = "hello"
#print(b)

#x = 10

#y = 4.8

#z = 4j

#print(x + y)
#print(x - y)
#print(x * y)
#print(x % y)

#print(x>y)

#name = "green"
#print(name[0])

#Fruits = ['apple', 'grapes', 'lemon']
#print(Fruits)
#for Fruit in Fruits:
 #   print(Fruit)

#foods = {1 : 'rice', 2 : 'beans' }
#print(foods)
#print(foods[2])

#myset = {1, 2, 4, 'goat', 'goat'}
#print(myset)

#for i in range (5) :
 #   print (i)

#students_score = [1, 2, 3, 4, 5, 6, 7]
#for score in students_score: 
  #  score = score * 5
 #   print(score) 

#Even_odd = [1, 4, 5, 13, 23, 9, 10]
#even = 0
#odd = 0
#for x in Even_odd:
    #if x% 2 == 0:
   #     even = even + 1
  #  if x%3 == 0:
 #       odd = odd + 1
#print('the number of even is', even)
#print('the number of odd is', odd)



#print(type(z))


#the score of passed student

student_grades = [70, 50, 40, 60, 20, 30]
passed_student = 0
for x in student_grades: 
    if x > 64:
        passed_student = passed_student + 1
print('The number of passed student =', passed_student)

#namedturple
from collections import namedtuple
a = namedtuple ('courses', 'name, technology')
s = a ('data science', 'python')
print(s)

#deque
from collections import deque
a = ['e', 'd', 'u', 'h']
d = deque(a)
print(d)
d.appendleft ('a')
print(d)
d.popleft ()
print(d)

#chainmap to compute 2 ariables into a single views 
from collections import ChainMap
a = {1: 'edureka', 2: 'python'}
b = {3: 'ML', 4: 'AI'}
ai = ChainMap(a,b)
print(ai)

#counter to count the number of time hashable objects appears 
from collections import Counter
c = [1, 1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,6,6,]
e = Counter(c)
print(e)
print(list(e.elements()))
print(list(e.most_common()))

#orderedDict is subclass which remembred the order 
from collections import OrderedDict
d = OrderedDict ()
d[1] ='g'
d[2] = 'r'
d[3] = 'e'
d[4] = 'e'
d[5] = 'n'
print(d)
print(d.values())

#defaultdict is a dictionary subclass which calls a factory function to supply missing values 
from collections import defaultdict
d = defaultdict(int)
d[1] = 'python'
d[2] = 'ai'

print(d)

#UserDict is a wrapper around dictionary objects for easier dictionary sub-classing 
#UserList is a wrapper around list objects for easier list sub-classing 
#UserString is a wrapper around string objets for easier string sub-classing


 

