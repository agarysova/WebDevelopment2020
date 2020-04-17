import { Component, OnInit } from '@angular/core';
import {Vacancy} from '../interfaces/vacancy';
import {CompaniesService} from '../companies.service';
import {ActivatedRoute} from '@angular/router';
import {CompanyVacancies} from '../interfaces/company_vacancies';

@Component({
  selector: 'app-company-vacancies',
  templateUrl: './company-vacancies.component.html',
  styleUrls: ['./company-vacancies.component.css']
})
export class CompanyVacanciesComponent implements OnInit {

  companyVacancies: CompanyVacancies;
  constructor(private companiesService: CompaniesService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getVacancies();
  }

  getVacancies(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.companiesService.getCompanyVacancies(id).subscribe(companyVacancies => this.companyVacancies = companyVacancies);
  }
}
