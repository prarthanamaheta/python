
# #ABC
from abc import ABC, abstractmethod

class AbstractClassName(ABC):

    # @abstractmethod
    def abstract_method(self):
        print("my abstract method")

    
    def abstract_method_1(self):
        print(" not abstract method")
 
class  Abstract1(AbstractClassName):
    pass

    # def abstract_method(self):
    #     print("abstracting class")


obj1=Abstract1()
obj1.abstract_method()
# obj1.abstract_method_1()



# class Random:
#     def __init__(self, **args):
#         print(args)
#         self.a = args.get('positional_first', 1)
#         self.b = args.get('positional_second', 2)
#         # self.n = args.get('num') 

#     @classmethod
#     def named_const_1_param(cls, positional_second):
#         cls(positional_second=positional_second).addition() 

#     @classmethod 
#     def named_const_2_param(cls, positional_first):
#         cls(positional_first=positional_first).addition()

#     def addition(self):
#         print(self.a + self.b)

#     def negative(num):
#         sum=(filter(lambda n: n<0,num))
#         print(list(sum))


#     def out():
        
#         x ="00000"

#         def inn():
#             nonlocal x
#             x = "11111"
#             print(x)
#         inn()
#         print(x)

#         def g():
#             global x
#             x = "11111 "
#             print(x)
#         inn()
#         print(x)
    
#     out()
            
# if __name__ == '__main__':
#     class_obj = Random
#     class_obj.named_const_1_param(2)
#     class_obj.named_const_2_param(1)
#     class_obj.negative([-1,2,-3])
#     class_obj.out() 
