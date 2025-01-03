# A=(1,2,3,4,5)
# print(A[1:4])
# #A.append([2,3,4,5])
# print(A)

# mySet = {"A","A"}
# print(mySet)
# mySet = {'a','b'} &{'a'}
# print(mySet)

# L = ['c','d']
# L.append(['a','b'])
# print(L)

# A=["hard rock",10,1.2]
# del(A[1])
# print(A)

# print(len(("disco",10)))

# myDict = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
# print(myDict.values())

# for x in range(0, 3):
#     print(x)

# for i, x in enumerate(['A', 'B', 'C']):
#     print(i, x)

# print(len([sum([1,1,1])]))
# L=[1,3,2]
# sorted(L)
# print(L) 

# class Vehicle:
#     color = "white"


#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.seating_capacity = None


#     def assign_seating_capacity(self, seating_capacity):
#         self.seating_capacity = seating_capacity


# V1 = Vehicle(150, 25)
# print(V1.color)

# class Circle(object):
#     # Constructor
#     def __init__(self, radius=3, color='blue'):
#         self.radius = radius
#         self.color = color
        
#     # Method
#     def add_radius(self, r):
#         self.radius = self.radius + r
#         return self.radius
    
# CircleObject = Circle()
# CircleObject.radius = 10
# print(CircleObject.radius, CircleObject.color)

# import string

# # Sample string with punctuation
# text = "Hello, world! How's it going?"

# # Create a translation table that maps each punctuation to None
# translator = str.maketrans('', '', string.punctuation)
# print(translator)
# # Use translate to remove punctuation
# cleaned_text = text.translate(translator)

# print(cleaned_text)  # Output: "Hello world Hows it going"

for i, x in enumerate(['A', 'B', 'C']): 
    print(i, 2 * x)