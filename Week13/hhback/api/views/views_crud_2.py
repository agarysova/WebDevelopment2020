# import json
# from django.http.response import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
#
# from api.models import Company, Vacancy
# from api.serializers import CompanySerializer
#
#
# @csrf_exempt
# def companies_list(request):
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         serializer = CompanySerializer(companies, many=True)
#
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         request_body = json.loads(request.body)
#
#         serializer = CompanySerializer(data=request_body)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#
#         return JsonResponse({'error': serializer.errors})
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
#         serializer = CompanySerializer(company)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         request_body = json.loads(request.body)
#
#         serializer = CompanySerializer(instance=company, data=request_body)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse({'error': serializer.errors})
#
#     elif request.method == 'DELETE':
#         company.delete()
#
#         return JsonResponse({'deleted': True})










