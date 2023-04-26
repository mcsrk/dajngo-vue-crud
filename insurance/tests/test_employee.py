from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
from insurance.models import Company, Admin, Branch, Employee
from insurance.serializers import EmployeeSerializer

# CRUD tests for Employee


class EmployeeAPITestCase(APITestCase):
    client = APIClient()

    def setUp(self):
        self.admin = Admin.objects.create(
            admin_name="John",
            admin_username="johndoe",
            admin_password="password",
            admin_email="john@example.com"
        )

        self.company = Company.objects.create(
            company_name="Test Company",
            company_email="test@example.com",
            admin=self.admin
        )

        self.branch = Branch.objects.create(
            branch_name="Test Branch",
            branch_city="Test City",
            branch_phone="1234567890",
            company=self.company
        )

        self.employee = Employee.objects.create(
            employee_name="John Smith",
            employee_phone="1234567890",
            employee_uid="ABCD1234",
            employee_email="john@example.com",
            branch=self.branch
        )

        self.valid_payload = {
            'employee_name': 'Updated Employee Name',
            'employee_phone': '0987654321',
            'employee_uid': 'WXYZ5678',
            'employee_email': 'updated-email@example.com',
            'branch': self.branch.branch_id
        }

        self.invalid_payload = {
            'employee_name': '',
            'employee_phone': 'invalid-phone',
            'employee_uid': 'invalid-uid',
            'employee_email': 'invalid-email',
            'branch': 999  # Non-existent branch ID
        }

    def test_get_all_employees(self):
        # Ensure we can get all employees
        response = self.client.get(reverse('employees-list'))
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_employee(self):
        # Ensure we can get a single employee with a valid ID
        response = self.client.get(
            reverse('employees-detail', args=[self.employee.employee_id]))
        employee = Employee.objects.get(employee_id=self.employee.employee_id)
        serializer = EmployeeSerializer(employee)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_employee(self):
        # Ensure we get a 404 response when requesting an employee with an invalid ID
        response = self.client.get(reverse('employees-detail', args=[1000]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_employee(self):
        # Ensure we can create a new employee with valid data
        response = self.client.post(
            reverse('employees-list'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_employee(self):
        # Ensure we get a 400 response when trying to create an employee with invalid data
        response = self.client.post(
            reverse('employees-list'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_employee(self):
        # Ensure we can delete an existing employee
        response = self.client.delete(
            reverse('employees-detail', args=[self.employee.employee_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure the employee no longer exists in the database
        with self.assertRaises(Employee.DoesNotExist):
            Employee.objects.get(employee_id=self.employee.employee_id)

    def test_delete_invalid_employee(self):
        # Ensure we get a 404 response when trying to delete an employee with an invalid ID
        response = self.client.delete(reverse('employees-detail', args=[1000]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
