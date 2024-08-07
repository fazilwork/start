# class parents:
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age
#     def text(self):
#         return f"имя  {self.__name} возраст {self.age}"
        

# class children(parents):
#     def __init__(self, name, age,hobby):
#         super().__init__(name, age)
#         self.hobby= hobby

#     def text_chil(self):
#         return f"мой возраст {self.age} имя {self.name}"

# child = children("boto",14,"wer")
# print(child.text())
# print("  ")
# print(child.text_chil()) 




class person:
    def skin_color(self):
        return "color"

class white:
    def skin_color(self):
        return "while"    
class red:
    def skin_color(self):
        return "red"
class black:
    def skin_color(self):
        return "negrrrr"
    
human = [person(),white(),red(),black()]
for x  in human:
    print(x.skin_color())    







