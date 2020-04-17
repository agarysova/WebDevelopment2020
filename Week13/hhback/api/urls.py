from django.urls import path
# from api.views import companies_list, company_details

from api.views.views_fbv import companies_list, company_details, company_vacancies, vacancies_list, vacancy_detail, \
    vacancies_top
from api.views.views_cbv import CompaniesList, CompanyDetails, VacanciesList, VacancyDetail, VacanciesTop, \
    CompanyVacancies
from api.views.views_generic import CompaniesListAPIView, CompanyDetailsAPIView, VacanciesListAPIView, \
    VacancyDetailsAPIView, CompanyVacanciesAPIView

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),

    path('login/', obtain_jwt_token),
    path('companies/', CompaniesListAPIView.as_view()),
    path('companies/<int:id>/', CompanyDetailsAPIView.as_view()),
    path('companies/<int:id>/vacancies/', CompanyVacanciesAPIView.as_view()),

    path('vacancies/', VacanciesListAPIView.as_view()),
    path('vacancies/<int:id>/', VacancyDetailsAPIView.as_view()),
    path('vacancies/top_ten/', VacanciesTop.as_view()),


    # path('companies/', CompaniesList.as_view()),
    # path('companies/<int:company_id>/', CompanyDetails.as_view()),
    # path('companies/<int:company_id>/vacancies/', CompanyVacancies.as_view()),
    #
    # path('vacancies/', VacanciesList.as_view()),
    # path('vacancies/<int:vacancy_id>/', VacancyDetail.as_view()),
    # path('vacancies/top_ten/', VacanciesTop.as_view())


    # path('companies/', companies_list),
    # path('companies/<int:company_id>/', company_details),
    # path('companies/<int:company_id>/vacancies/', company_vacancies),

    # path('vacancies/', vacancies_list),
    # path('vacancies/<int:vacancy_id/>', vacancy_detail),
    # path('vacancies/top_ten/', vacancies_top)

]
