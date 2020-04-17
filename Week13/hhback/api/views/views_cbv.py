from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancyModelSerializer


class CompaniesList(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        request_body = json.loads(request.body)
        serializer = CompanySerializer(data=request_body, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})


class CompanyDetails(APIView):

    def get_company(self, company_id):
        try:
            return Company.objects.get(id=company_id)
        except Exception as e:
            return Response({'error': str(e)})

    def get(self, request, company_id):
        try:
            serializer = CompanySerializer(self.get_company(company_id))
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return Response({'error': str(e)})

    def put(self, request, company_id):
        try:
            request_body = json.loads(request.body)
            serializer = CompanySerializer(instance=self.get_company(company_id), data=request_body)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return JsonResponse({'error': serializer.errors})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    def delete(self, request, company_id):
        try:
            self.get_company(company_id).delete()
            return JsonResponse({'delete': True})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class VacanciesList(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancyModelSerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})


class VacancyDetail(APIView):

    def get_vacancy(self, vacancy_id):
        try:
            return Vacancy.objects.get(id=vacancy_id)
        except Exception as e:
            return JsonResponse({'error': str(e)})

    def get(self, request, vacancy_id):
        try:
            serializer = VacancyModelSerializer(self.get_vacancy(vacancy_id))
            return Response(serializer.data)
        except Exception as e:
            return JsonResponse({'error': str(e)})

    def put(self, request, vacancy_id):
        serializer = VacancyModelSerializer(instance=self.get_vacancy(vacancy_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, vacancy_id):
        try:
            self.get_vacancy(vacancy_id).delete()
            return JsonResponse({'delete': True})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class VacanciesTop(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancyModelSerializer(vacancies, many=True)
        return Response(serializer.data)


class CompanyVacancies(APIView):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id)
            vacancies = company.vacancies.all()
            serializer = VacancyModelSerializer(vacancies, many=True)
            return Response(serializer.data)
        except Exception as e:
            return JsonResponse({'error': str(e)})
