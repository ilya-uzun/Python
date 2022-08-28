from unittest import TestCase, main
from calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('16-1'), 15)

    def test_multiply(self):
        self.assertEqual(calculator('3*3'), 9)

    def test_divide(self):
        self.assertEqual(calculator('200/2'), 100)

    # Проверка исключения
    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('11111')
        self.assertEqual('Вырожение должно содержать минимум один знак (+-/*)', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Вырожение должно содержать два целых числа и один знак', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('1+3*3')
        self.assertEqual('Вырожение должно содержать два целых числа и один знак', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.2 - 3.3')
        self.assertEqual('Вырожение должно содержать два целых числа и один знак', e.exception.args[0])

if __name__ == '__main__':
    main()
