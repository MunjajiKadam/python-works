
import abc


class batch1:
    @abc.abstractmethod
    def batch1_method(self):
        pass
    @abc.abstractmethod
    def batch1_method2(self):
        pass

class batch2(batch1):
    def batch1_method(self):
        return "this is batch1 method from batch2"
    def batch1_method2(self):
        return "this is batch1 method2 from batch2"

class batch3(batch2):
    def batch1_method(self):
        return "this is batch1 method from batch3"
    def batch1_method2(self):
        return "this is batch1 method2 from batch3"

batch3_obj = batch3()
batch2_obj = batch2()

print(batch3_obj.batch1_method())  # Output: "this is batch1 method from batch3"
print(batch3_obj.batch1_method2())  # Output: "this is batch1 method2 from batch3"

print(batch2_obj.batch1_method())  # Output: "this is batch1 method from batch2"
print(batch2_obj.batch1_method2())  # Output: "this is batch1 method2 from batch2"