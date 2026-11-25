import unittest
from zion.lexer import lex

class LexerTests(unittest.TestCase):
    def test_skips_blank_and_comment_lines(self):
        lines = lex('# comment\n\nSay "Hi"\n')
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0].text, 'Say "Hi"')
        self.assertEqual(lines[0].number, 3)

if __name__ == '__main__':
    unittest.main()
