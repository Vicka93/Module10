import unittest
from class_definitions import student as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t.Student('Denys', 'Daisy', 'English',4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Denys')
        self.assertEqual(self.student.first_name, 'Daisy')
        self.assertEqual(self.student.major, 'English')
        

    def test_object_created_all_attributes(self):
        self.assertEqual(True, False)

    def test_student_str(self):
        self.assertEqual(True, False)

    def test_object_not_created_error_last_name(self):
        self.assertEqual(True, False)

    def test_object_not_created_error_first_name(self):
        self.assertEqual(True, False)

    def test_object_not_created_error_major(self):
        self.assertEqual(True, False)

    def test_object_not_created_error_gpa(self):
            self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
