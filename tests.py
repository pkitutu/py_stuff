'''Module for testing functions in python stuff'''

import unittest
from humanize_duration import humanize_duration
from valid_braces import valid_braces


class TestPyStuff(unittest.TestCase):
    ''' Class for testing functions in python stuff '''

    def test_humanize_duration(self):
        ''' Test humanize duration function'''
        checks = [
            {'input': 0, 'expected': 'now'},
            {'input': 1, 'expected': '1 second'},
            {'input': 60, 'expected': '1 minute'},
            {'input': 3600, 'expected': '1 hour'},
            {'input': 86400, 'expected': '1 day'},
            {'input': 31536000, 'expected': '1 year'},
            {'input': 31536001, 'expected': '1 year and 1 second'},
            {'input': 500000000, 'expected': '15 years, 312 days, 53 minutes and 20 seconds'},
            ]
        for check in checks:
            result = humanize_duration(check['input'])
            msg = f'Expecting {check["expected"]}, but got {result}'
            self.assertEqual(result, check['expected'], msg)

    def test_valid_braces(self):
        self.assertTrue(valid_braces(''), 'expected True')
        self.assertTrue(valid_braces('{}'), 'expected True')
        self.assertTrue(valid_braces('{}()[]{{{{([])}}}}'), 'expected True')
        self.assertFalse(valid_braces('('), 'expected False')
        self.assertFalse(valid_braces(']{{}}(())'), 'expected False')


if __name__ == '__main__':
    unittest.main()
