from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models import Company, Vacancy

from api.serializers import CompanyModelSerializer, VacancyModelSerializer, CompanyVacanciesSerializer


class CompaniesListAPIView(generics.ListCreateAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanyModelSerializer
	permission_classes = (IsAuthenticated, )


class CompanyDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanyModelSerializer
	lookup_url_kwarg = 'id'


class VacanciesListAPIView(generics.ListCreateAPIView):
	queryset = Vacancy.objects.all()
	serializer_class = VacancyModelSerializer


class VacancyDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Vacancy.objects.all()
	serializer_class = VacancyModelSerializer
	lookup_url_kwarg = 'id'


class CompanyVacanciesAPIView(generics.RetrieveAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanyVacanciesSerializer
	lookup_url_kwarg = 'id'