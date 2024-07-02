class Student():#To define a class in Python, you use class the keyword.

    # Class variable
    school_name="1 No School"
    
    # static methods
    @staticmethod
    def is_adult_age(student):
         if student.age > 18:
          return  "_allowed_" 
         else:
          return "_don't allowed_" 


    # constructor
    def __init__(self,name,age,address,roll_no) :
    # The __init__() function is called automatically every time the class is being used to create a new object.
      self.name=name
      self.age=age
      self.address=address
      self.roll_no=roll_no


    # Instance methods
    def say_about_you(self):
       return (f"My name is {self.name} and age is {self.age}")
    
    def programming_skill(self,python_skill=False):
       if python_skill  :
          return f"{self.name} know about python programming language"
       else:
          return f"{self.name} don't know about python programming language"
       
    def can_song(self,skill=False):
         if skill ==True :
          return f"{self.name} can song music"
         else:
          return f"{self.name} cannot song music"
          


################################################################################################
# three Objects created  
student_1 = Student("Hasan",15,"Baki","322718")
student_2 = Student("Zaman",17,"Quba","296584")
student_3 = Student("Qasim",16,"Lenkeran","289658")

# Access Object Methos
print(student_1.say_about_you())
print(student_1.programming_skill(True))
print(student_3.can_song(skill=True))
print(student_2.can_song(skill=False))

# Modify Object Properties
student_1.name="Ramazan"

# Delete Object Properties
del student_1.roll_no

# default control age limit
print(Student.is_adult_age(student_1))
print(Student.is_adult_age(student_2))
print(Student.is_adult_age(student_3))