import importlib

importlib.import_module("hello")

class TestCase():
    def setUp(self):
        return self.assertEqual(hello.hi(), "Hello World!!")

