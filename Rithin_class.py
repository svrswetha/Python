"""def is_multiply(x,y):
  if ((x!=0) & (y%x)==0):
    print True
  else:
    print False
  print("A python is a program")


x= int(input("Enter a number: "))
print(x)
y = int(input("Enter a multiple: "))
print("mult of x is", y)

is_multiply(x,y)

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        break
    else:


# Modify this function to return a list of strings as defined above
def list_benefits():
  return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
  return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
  list_of_benefits = list_benefits()
  for benefit in list_of_benefits:
    print(build_sentence(benefit))


name_the_benefits_of_functions()

class Myclass:
  var = "blahblah"
  def func(self):
    print "I am a self function"
myobject = Myclass()
myobject.func()

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 =Vehicle()
car1.name = "Fer"
car1.color = "red convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue van"
car2.value = 10000.00
# test code
print(car1.description())
print(car2.description())
"""
#Dictionaries
phonebook ={
  "John": 938477566,
  "Jack": 938377264,
  "Jill": 947662781
}

print phonebook

for name,number in phonebook.items():
  print("%s phone number is %d" %(name, number))

del phonebook["John"]
"""phonebook.pop('John')"""
print phonebook
#add a item use update with curly braces
phonebook.update({"Jake":938273443})
del phonebook["Jill"]
#phonebook["Jake",938273443]
print phonebook
