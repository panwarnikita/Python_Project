# student = {
#     "name" : "Mayuri Tupe",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 98,
#         "math" : 95
#     }
# }

# new_dict = {"name" : "Nikku", "age" : 16}
# student.update(student)
# print(student)
# print(student.get("key"))


# value = {9,9.25, 8, 8.0}
# print(value)



# def s(a, b):
#     sum = a+b
#     return sum
# print(s(2, 3))



# def type(n):
#     if(n%2!=0):
#       return "odd"
#     else:
#        return "even"
# print(type(4))



# def count(n):
#     if n == 0:
#         return
#     print(n)
#     count(n-1)
# count(5)


# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1)*n
# print(fact(1))



# def calc_sum(n):
#     if(n==0):
#        return 0
#     return calc_sum(n-1)+n
# sum = calc_sum(10)
# print(sum)


# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)
# fruits = ["mango", "litch", "apple", "banana"]
# print_list(fruits)




# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course



# class Student:
#     name = "Kanuu"

# s1 = Student()
# print(s1.name)




# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg  score is:", sum/3)
# s1 = Student("today stark", [99, 98, 97])
# s1.get_avg()



# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch  = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started..")
# ca1 = Car()
# ca1.start()



# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

# acc1 = Account(10000, 12345)
# print(acc1.balance)
# print(acc1.account_no)



# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
        
# s1 = Student("Nikita", 20,"Python")
# s2 = Student("Amana", 21, "Java")

# print(s1.name)
# print(s1.course)




# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
# s1.name
# s2.name
        





# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         return sum(self.marks)/len(self.marks)

# s1 = Student("Nikita", [80,90,85])
# print(s1.average())





# class Student:
#     @staticmethod
#     def college():
#         print("ABCDEF")
# Student.college()




# class Account:
#     def __init__(self, balance):
#         self.balance = balance

#     def debit(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount



