import unittest
from lab import calculate_age, calculate_grade
from teamb import process_student_data
class Testunittest(unittest.TestCase):
    # Test for calculate_age
    def test_calculate_age(self):
        self.assertEqual(calculate_age(2004), 20)
        self.assertEqual(calculate_age(2024), 0)  
        self.assertEqual(calculate_age(1900), 124) 
        
    def test_calculate_grade(self):
        self.assertEqual(calculate_grade(95), "A")
        self.assertEqual(calculate_grade(80), "A") 
        self.assertEqual(calculate_grade(75), "B+") 
        self.assertEqual(calculate_grade(70), "B") 
        self.assertEqual(calculate_grade(65), "C+") 
        self.assertEqual(calculate_grade(60), "C") 
        self.assertEqual(calculate_grade(55), "D+")  
        self.assertEqual(calculate_grade(50), "D") 
        self.assertEqual(calculate_grade(49), "F")  
        self.assertEqual(calculate_grade(0), "F") 

class TestFileProcessing(unittest.TestCase):
    def test_process_student_data(self):
        # Open and read the 'lab.txt' file
        with open("lab.txt", "r") as file:
            data = file.readlines()
        
        result = process_student_data(data)
        # Test the processed data
        self.assertEqual(result["buddhist_era"], 2547)  # 2024 - 20 + 543
        self.assertEqual(result["rank"], "Distinction")
        
if __name__ == "__main__":
    unittest.main()