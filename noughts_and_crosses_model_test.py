import unittest
from one_player_noughts_and_crosses import is_line_winning
from one_player_noughts_and_crosses import check_row
from one_player_noughts_and_crosses import check_others

Grid=[['x','o','o'], ['x','o','o'], ['o','x','x']]
x=3
y=1

class Test(unittest.TestCase):

    def test_check_row(self):
        Target=['o','x','x']
        self.assertEqual(Target,check_row(Grid,x),"This function fails to output the correct row.")

    def test_check_column(self):
        Target=['x','x','o']
        self.assertEqual(Target,check_others(Grid,y,'Vertical'),"This function fails to output the correct column.")

    def test_check_diag_forward(self):
        Target=['x','o','x']
        self.assertEqual(Target,check_others(Grid,y,'Diag_forward'),"This function fails to output the leading diagonal.")

    def test_check_diag_backward(self):
        Target=['o','o','o']
        self.assertEqual(Target,check_others(Grid,y,'Diag_backward'),"This function fails to output the reverse diagonal.")

    def test_is_line_winning(self):
        goodLine=['x','x','x']
        badLine=['x','o','x']
        self.assertEqual(is_line_winning(goodLine),True,"This function erroneously excludes winning lines.")
        self.assertEqual(is_line_winning(badLine),False,"The function erroneously labels non-winning lines as having won.")

unittest.main()
