from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Company, Vacancy


def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()

    companies_json = [company.to_json() for company in companies]
    data = {
        'companies': companies_json,
    }
    return JsonResponse(data)


def company_details(request, company_id):
    try:
        company = Company.objects.get(id=company_id).to_json()

    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(company)


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(vacancy.to_json())


def company_vacancies(request, company_id):
    vacancies = Vacancy.objects.filter(company=company_id)
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancies_top_ten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)
