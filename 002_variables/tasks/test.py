import os
import unittest
import task01
import task02
import gk.assignments.assignment as assignment
from gk.GkTest import GkTest


class MyTestCase(GkTest):

    def test_task_01(self):
        test_set = [(1, 1), (2, 5), (3, 5), (125, 9)]
        answers = {}
        for test in test_set:
            base = test[0]
            h = test[1]
            i = 0

            def side_effect(s):
                nonlocal base, h, i
                if i == 0:
                    i += 1
                    return base
                return h

            y = round(float(super().wrapper_with_side_effect(lambda: task01.task(), side_effect)), 2)
            answers[f'%s %s' % (base, h)] = str(y)
        print(answers)
        self.assertEqual(assignment.check_assignment(5, 1, 'Square root', answers), True)


    def test_task_02(self):
        test_set = [(100, 1), (100, 50), (100, 100), (50, 50), (100, 0)]
        answers = {}
        for test in test_set:
            price = test[0]
            percent = test[1]
            i = 0

            def side_effect(s):
                nonlocal i, price, percent
                if i == 0:
                    i += 1
                    return price
                return percent

            y = round(float(super().wrapper_with_side_effect(lambda: task02.task(), side_effect)), 2)
            answers[f'%s %s' % (price, percent)] = str(y)
        print(answers)
        self.assertEqual(assignment.check_assignment(5, 1, 'Square root', answers), True)


os.chdir('../..')
if __name__ == '__main__':
    unittest.main()