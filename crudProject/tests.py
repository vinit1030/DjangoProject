from django.test import TestCase

from crudProject.models import crudEmployee
from .import views

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        crudEmployee.objects.create(ename='Vinit', eaddress='Hyderabad', age=30, egender='M')

    def test_e_name_label(self):
        employee = crudEmployee.objects.get(id=1)
        field_label = employee._meta.get_field('ename').verbose_name
        self.assertEqual(field_label, 'Employee Name')

    def test_age_label(self):
        employee = crudEmployee.objects.get(id=1)
        field_label = employee._meta.get_field('age').verbose_name
        self.assertEqual(field_label, 'age')

    def test_employee_display(self):
        employee = crudEmployee.objects.all()
        self.assertEqual(len(employee), 1)