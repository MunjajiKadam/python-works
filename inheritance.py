#inheritance in python
class parent:
     def func1(self):
         print("This function is in parent class.")

class child( parent):
        pass        

child_obj = child()
child_obj.func1()
            