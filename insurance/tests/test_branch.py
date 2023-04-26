from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
from insurance.models import Company, Admin, Branch
from insurance.serializers import BranchSerializer

# CRUD Test for Branch

class BranchAPITestCase(APITestCase):
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
            branch_phone="12345678",
            company=self.company
        )

        self.valid_payload = {
            'branch_name': 'Updated Branch Name',
            'branch_city': 'Updated City',
            'branch_phone': '87654321',
            'company': self.company.company_id
        }

        self.invalid_payload = {
            'branch_name': '',
            'branch_city': 'Test City',
            'branch_phone': '12345678',
            'company': 999  # Non-existent company ID
        }

    def test_get_all_branches(self):
        # Ensure we can get all branches
        response = self.client.get(reverse('branches-list'))
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_branch(self):
        # Ensure we can get a single branch with a valid ID
        response = self.client.get(
            reverse('branches-detail', args=[self.branch.branch_id]))
        branch = Branch.objects.get(branch_id=self.branch.branch_id)
        serializer = BranchSerializer(branch)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_branch(self):
        # Ensure we get a 404 response when requesting a branch with an invalid ID
        response = self.client.get(reverse('branches-detail', args=[1000]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_branch(self):
        # Ensure we can create a new branch with valid data
        response = self.client.post(
            reverse('branches-list'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_branch(self):
        # Ensure we get a 400 response when trying to create a branch with invalid data
        response = self.client.post(
            reverse('branches-list'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_branch(self):
        # Ensure we can update an existing branch
        response = self.client.put(
            reverse('branches-detail', args=[self.branch.branch_id]),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_branch(self):
        # Ensure we can delete a branch
        response = self.client.delete(
            reverse('branches-detail', args=[self.branch.branch_id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
