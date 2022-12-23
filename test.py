import unittest
from biurko import Biurko

class BiurkoTest(unittest.TestCase):
    def test_can_choose_material(self):
        biurko = Biurko()
        biurko.wybierz_material('szklo')
        self.assertEqual('szklo', biurko.moje_materialy())

if __name__ == '__main__':
    unittest.main()
