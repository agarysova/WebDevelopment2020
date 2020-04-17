import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {CompaniesListComponent} from './companies-list/companies-list.component';
import {CompanyVacanciesComponent} from './company-vacancies/company-vacancies.component';


const routes: Routes = [
 // {path: '', redirectTo: 'api2/companies/', pathMatch: 'full'},
  {path: '', component: CompaniesListComponent},
  {path: 'companies/:id/vacancies', component: CompanyVacanciesComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
