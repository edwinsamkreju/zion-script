import unittest
from zion.compiler import transpile
from zion.errors import ZionError

class CompilerTests(unittest.TestCase):
    def test_say(self):
        self.assertIn('print("Hello")', transpile('Say "Hello"'))

    def test_store_and_condition(self):
        source = 'Store 8 as score\nIf score is greater than 5\n    Say "yes"\nOtherwise\n    Say "no"\nEnd if\n'
        code = transpile(source)
        self.assertIn('score = 8', code)
        self.assertIn('if score > 5:', code)

    def test_repeat(self):
        code = transpile('Repeat 3 times\n    Say "go"\nEnd repeat\n')
        self.assertIn('range(int(3))', code)

    def test_lists(self):
        source = 'Create a list called pets\nAdd "cat" to pets\nFor each pet in pets\n    Say pet\nEnd for\n'
        code = transpile(source)
        self.assertIn('pets.append("cat")', code)
        self.assertIn('for pet in pets:', code)

    def test_missing_end_if(self):
        with self.assertRaises(ZionError):
            transpile('If 2 > 1\n    Say "yes"\n')

if __name__ == '__main__':
    unittest.main()
