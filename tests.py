import importlib
import unittest

importlib.import_module("hello")

class TestCase(unittest.TestCase):
    def test(self):
        #result =  self.assertEqual(hello.hello_function(), "Hello World!!")
        result =  self.assertEqual(1, 1,"This is wrong")
        print(result)
        return result



MyTest = TestCase()
MyTest.test()
