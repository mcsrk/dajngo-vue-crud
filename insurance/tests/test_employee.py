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
            name="John",
            username="johndoe",
            password="password",
            email="john@example.com"
        )

        self.company = Company.objects.create(
            name="Test Company",
            email="test@example.com",
            admin=self.admin
        )

        self.branch = Branch.objects.create(
            name="Test Branch",
            city="Test City",
            phone="1234567890",
            company=self.company
        )

        self.employee = Employee.objects.create(
            name="John Smith",
            phone="1234567890",
            uid="ABCD1234",
            email="john@example.com",
            branch=self.branch
        )

        self.valid_payload = {
            'name': 'Updated Employee Name',
            'phone': '0987654321',
            'uid': 'WXYZ5678',
            'email': 'updated-email@example.com',
            'branch': self.branch.id
        }

        self.invalid_payload = {
            'name': '',
            'phone': 'invalid-phone',
            'uid': 'invalid-uid',
            'email': 'invalid-email',
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
            reverse('employees-detail', args=[self.employee.id]))
        employee = Employee.objects.get(id=self.employee.id)
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
            reverse('employees-detail', args=[self.employee.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure the employee no longer exists in the database
        with self.assertRaises(Employee.DoesNotExist):
            Employee.objects.get(id=self.employee.id)

    def test_delete_invalid_employee(self):
        # Ensure we get a 404 response when trying to delete an employee with an invalid ID
        response = self.client.delete(reverse('employees-detail', args=[1000]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
