import unittest
from class_definitions import student as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t.Student('Denys', 'Daisy', 'English')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Denys')
        self.assertEqual(self.student.first_name, 'Daisy')
        self.assertEqual(self.student.major, 'English')

    def test_object_created_all_attributes(self):
        student = t.Student('Denys', 'Daisy', 'English', 4.0)
        assert student.last_name == 'Denys'
        assert student.first_name == 'Daisy'
        assert student.major == 'English'
        assert student.gpa == 4.0

    def test_student_str(self):

        student = t.Student('Denys', 'Daisy', 'English',4.0)

        self.assertEqual(str(student),"Denys, Daisy has major English with gpa: 4.0")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student = t.Student('123denys', 'Daisy', 'English', 4.0)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            student = t.Student('Denys', '123daisy','English', 4.0)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            student = t.Student('Denys', 'Daisy','123',4.0)

    def test_object_not_created_error_gpa_high(self):
        with self.assertRaises(ValueError):
            student = t.Student('Denys', 'Daisy', 'English',4.5)

    def test_object_not_created_error_gpa_low(self):
        with self.assertRaises(ValueError):
            student = t.Student('Denys', 'Daisy', 'English',-4.5)

    def test_object_not_created_error_gpa_bad(self):
        with self.assertRaises(ValueError):
            student = t.Student('Denys', 'Daisy', 'English',"four")


if __name__ == '__main__':
    unittest.main()
