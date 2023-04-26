from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
from insurance.models import Company, Admin
from insurance.serializers import CompanySerializer

# Tests for company


class CompanyAPITestCase(APITestCase):
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

        self.valid_payload = {
            'name': 'Updated Company Name',
            'email': 'new-email@example.com',
            'admin': self.admin.id
        }

        self.invalid_payload = {
            'name': '',
            'email': 'invalid-email',
            'admin': 999  # Non-existent admin ID
        }

    def test_get_all_companies(self):
        # Ensure we can get all companies
        response = self.client.get(reverse('companies-list'))
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_company(self):
        # Ensure we can get a single company with a valid ID
        response = self.client.get(
            reverse('companies-detail', args=[self.company.id]))
        company = Company.objects.get(id=self.company.id)
        serializer = CompanySerializer(company)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_company(self):
        # Ensure we get a 404 response when requesting a company with an invalid ID
        response = self.client.get(reverse('companies-detail', args=[1000]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_company(self):
        # Ensure we can create a new company with valid data
        response = self.client.post(
            reverse('companies-list'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_company(self):
        # Ensure we get a 400 response when trying to create a company with invalid data
        response = self.client.post(
            reverse('companies-list'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_company(self):
        # Ensure we can update an existing company
        response = self.client.put(
            reverse('companies-detail', args=[self.company.id]),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_company(self):
        # Ensure we can delete a company
        response = self.client.delete(
            reverse('companies-detail', args=[self.company.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
