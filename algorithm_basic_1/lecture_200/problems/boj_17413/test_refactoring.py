from unittest import TestCase

from algorithm_basic_1.lecture_200.problems.boj_17413.refactoring import sol


class Test(TestCase):
    def test_sol(self):
        self.assertEqual('noojkeab enilno egduj', sol('baekjoon online judge'))
        self.assertEqual('<open>gat<close>', sol('<open>tag<close>'))
        self.assertEqual('<ab cd>fe hg<ij kl>', sol('<ab cd>ef gh<ij kl>'))
        self.assertEqual('1eno 2owt 3eerht rruof4 evif5 xis6', sol('one1 two2 three3 4fourr 5five 6six'))
        self.assertEqual('<int><max>7463847412<long long><max>7085774586302733229',
                         sol('<int><max>2147483647<long long><max>9223372036854775807'))
        self.assertEqual('<problem>31471<is hardest>melborp reve<end>',
                         sol('<problem>17413<is hardest>problem ever<end>'))
        self.assertEqual('<   space   >ecaps ecaps ecaps<    spa   c e>',
                         sol('<   space   >space space space<    spa   c e>'))
