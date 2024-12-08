import unittest
import lab

class TestLab(unittest.TestCase):
    # Test for calculate_age
    def test_calculate_age(self):
        self.assertEqual(lab.calculate_age(2004), 20)
        self.assertEqual(lab.calculate_age(2024), 0)  
        self.assertEqual(lab.calculate_age(1900), 124) 
        
    def test_calculate_grade_A(self):
        self.assertEqual(lab.calculate_grade(95), "A")
        self.assertEqual(lab.calculate_grade(80), "A")

    def test_calculate_grade_B_plus(self):
        self.assertEqual(lab.calculate_grade(78), "B+") 
        self.assertEqual(lab.calculate_grade(75), "B+")

    def test_calculate_grade_B(self):
        self.assertEqual(lab.calculate_grade(74), "B")  
        self.assertEqual(lab.calculate_grade(70), "B") 

    def test_calculate_grade_C_plus(self):
        self.assertEqual(lab.calculate_grade(69), "C+")
        self.assertEqual(lab.calculate_grade(65), "C+") 

    def test_calculate_grade_C(self):
        self.assertEqual(lab.calculate_grade(64), "C")
        self.assertEqual(lab.calculate_grade(60), "C") 

    def test_calculate_grade_D_plus(self):
        self.assertEqual(lab.calculate_grade(59), "D+")
        self.assertEqual(lab.calculate_grade(55), "D+") 

    def test_calculate_grade_D(self):
        self.assertEqual(lab.calculate_grade(54), "D")  
        self.assertEqual(lab.calculate_grade(50), "D") 

    def test_calculate_grade_F(self):
        self.assertEqual(lab.calculate_grade(49), "F")  
        self.assertEqual(lab.calculate_grade(0), "F")  
if __name__ == "__main__":
    unittest.main()
