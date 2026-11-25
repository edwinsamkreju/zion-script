import unittest
from zion.compiler import transpile
from zion.errors import ZionError

class CompilerTests(unittest.TestCase):
    def test_show_and_be_assignment(self):
        code = transpile('answer be 6 * 7\nshow answer')
        self.assertIn('answer = 6 * 7', code)
        self.assertIn('print(answer)', code)

    def test_equals_assignment_and_python_operators(self):
        source = '''import math
x = 2 ** 3 + 10 // 2
x += 1
y = x % 3
z = math.sqrt(81)
flag = x >= 10 and z == 9
bits = (5 << 1) | 1
same = z is not None
inside = 3 in [1, 2, 3]
'''
        namespace = {}
        exec(transpile(source), namespace)
        self.assertEqual(namespace["x"], 14)
        self.assertEqual(namespace["y"], 2)
        self.assertEqual(namespace["z"], 9)
        self.assertTrue(namespace["flag"])
        self.assertEqual(namespace["bits"], 11)
        self.assertTrue(namespace["same"])
        self.assertTrue(namespace["inside"])

    def test_if_else_and_friendly_comparison(self):
        code = transpile('score be 95\nIf score is greater than or equal to 90\n    show "pass"\nOtherwise\n    show "retry"\nEnd if')
        self.assertIn("if score >= 90:", code)

    def test_repeat(self):
        code = transpile('Repeat 3 times\n    Show "go"\nEnd repeat')
        self.assertIn("range(int(3))", code)

    def test_lists(self):
        source = 'Create a list called pets\nAdd "cat" to pets\nFor each pet in pets\n    Show pet\nEnd for'
        code = transpile(source)
        self.assertIn('pets.append("cat")', code)
        self.assertIn("for pet in pets:", code)

    def test_old_syntax_remains_compatible(self):
        code = transpile('Store 8 as score\nSay "yes"')
        self.assertIn("score = 8", code)
        self.assertIn('print("yes")', code)

    def test_missing_end_if(self):
        with self.assertRaises(ZionError):
            transpile('If 2 > 1\n    Show "yes"')

if __name__ == "__main__":
    unittest.main()
