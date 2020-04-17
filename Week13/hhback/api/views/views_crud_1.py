# import json
# from django.http.response import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
#
# from .models import Company, Vacancy
#
#
# @csrf_exempt
# def companies_list(request):
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         companies_json = [company.to_json() for company in companies]
#         data = {
#             'companies': companies_json,
#         }
#         return JsonResponse(data, safe=False)
#     elif request.method == 'POST':
#         request_body = json.loads(request.body)
#         new_company_name = request_body.get('name', 'Company default name')
#         company = Company.objects.create(name=new_company_name)
#         company = Company.objects.create(description=request_body.get('description'))
#         company = Company.objects.create(city=request_body.get('city'))
#         company = Company.objects.create(address=request_body.get('address'))
#
#         return JsonResponse(company.to_json())
#
#
# @csrf_exempt
# def company_details(request, company_id):
#     try:
#         company = Company.objects.get(id=company_id)
#     except Company.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#
#     if request.method == 'GET':
#         return JsonResponse(company.to_json())
#     elif request.method == 'PUT':
#         request_body = json.loads(request.body)
#         company.name = request_body.get('name', company.name)
#         company.save()
#         return JsonResponse(company.to_json())
#     elif request.method == 'DELETE':
#         company.delete()
#         return JsonResponse({'deleted': True})
#
#
# def vacancies_list(request):
#     vacancies = Vacancy.objects.all()
#     vacancies_json = [vacancy.to_json() for vacancy in vacancies]
#     return JsonResponse(vacancies_json, safe=False)
#
#
# def vacancy_details(request, vacancy_id):
#     try:
#         vacancy = Vacancy.objects.get(id=vacancy_id)
#
#     except Vacancy.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#
#     return JsonResponse(vacancy.to_json())
#
#
# def company_vacancies(request, company_id):
#     vacancies = Vacancy.objects.filter(company=company_id)
#     vacancies_json = [v.to_json() for v in vacancies]
#     return JsonResponse(vacancies_json, safe=False)
#
#
# def vacancies_top_ten(request):
#     vacancies = Vacancy.objects.all().order_by('-salary')[:10]
#     vacancies_json = [vacancy.to_json() for vacancy in vacancies]
#     return JsonResponse(vacancies_json, safe=False)
