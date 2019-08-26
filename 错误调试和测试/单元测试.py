import unittest

from D面向对象.实例属性与类属性 import Student
# from 错误调试和测试 import 错误处理


class TestStudent(unittest.TestCase):
    def test_init(self):
        s1 = Student('老司机')
        self.assertEqual(s1.s_name, '老司机')
        self.assertTrue(True, True)

    # def test_错误处理(self):
    #     错误处理
    #     with self.assertRaises(ZeroDivisionError):
    #         print('确实发生了异常，测试通过')

    def setUp(self) -> None:
        print('测试之前我必运行')

    def tearDown(self) -> None:
        print('测试完成之后我必运行')
