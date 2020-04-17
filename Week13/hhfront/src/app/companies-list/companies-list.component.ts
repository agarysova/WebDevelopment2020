import { Component, OnInit } from '@angular/core';
import {CompaniesService} from '../companies.service';
import {Company} from '../interfaces/company';

@Component({
  selector: 'app-companies-list',
  templateUrl: './companies-list.component.html',
  styleUrls: ['./companies-list.component.css']
})
export class CompaniesListComponent implements OnInit {
companies: Company[] = [];
  constructor(private companiesService: CompaniesService) { }

  ngOnInit(): void {
    this.getCompanies();
  }

  getCompanies(): void {
    this.companiesService.getCompanies().subscribe(companies => this.companies = companies);
  }

}
