#                                                     ПЕРВЫЙ 
# class Book:
#     def __init__(self ,title,auh,year,page):
#         self.title = title
#         self.auh = auh
#         self.year = year
#         self.page = page
#     def age(title,auh,year,page):
#         if  year >= year - 20:
#             print("книга старше 20 лет")
#             print(f"тем {title}, афтора зовут {auh}, страниц {page}, книга {year} года" )
#         else:
#             print("книга младше")
#             print(f"тем {title}, афтора зовут {auh}, страниц {page}, книга {year} года" )
        
            
# book = Book.age(234,4234,234,234)        
# print(book)

#                                                        второй

# class banc_Control:
#     def __init__(self, holder, number , balanc ): 
#         self.holder = holder
#         self.number = number
#         self.balans = balanc
#     def popol(self, popola):
#         if popola > 0:
#             self.balans = self.balans + popola
#             print(f"ваш счет пополнен на {popola} ваш счет теперь {self.balans}")
#         else:
#             print(f"у вас не хватает денег для пополнения и ваш счет составляет {self.balans}")
#     def vichit (self, vich):
#         self.vich = vich
#         if vich < self.balans:
#             self.balans =- vich
#             print(f"у вас на счету осталось {self.balans}")
#         else:
#             print(f"у вас нету достаточно средств для вывода")   
#     def snitia(self, snt):
#         if self.balans >= snt:
#            self.balans = self.balans - snt
#            print(f"у вас на счету осталось {self.balans} вы сняли {snt}")
#         else:
#             b = self.balans - snt

#             print(f"у вас не хватает чтобы снять у вас пока {self.balans} вам еще нужно {b}" )        


acc = banc_Control(holder =100, number = 1231, balanc = 1000 )
acc.popol(200)
acc.snitia(300)
acc.vichit(22000)

class student:
    def __init__(self,student_name , student_id,student_value):
        self.student_name = student_name
        self.student_id = student_id
        self.student_value = student_value                
    def ratings (self):
        self.student_ratings = student_ratings
        student_ratings = []
        value1 = input()
        if value1 <= 5:
            student_ratings.append(value1)
        else:
            print("у нас 5 бальная система пиши нормально неучь")    
        value2 = input()
        if value2 <= 5:
            student_ratings.append(value2)
        else:
            print("у нас 5 бальная система пиши нормально неучь")  
            
        value3 = input()
        if value3 <= 5:
            student_ratings.append(value3)     
        else:
            print("у нас 5 бальная система пиши нормально неучь")  
    def summaaa(selfstudent_ratings):
        student_ratings.






