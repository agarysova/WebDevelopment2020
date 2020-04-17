import {Injectable} from '@angular/core';
import {Company} from './interfaces/company';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {CompanyVacancies} from './interfaces/company_vacancies';
import {LoginResponse} from './interfaces/login';

@Injectable({
  providedIn: 'root'
})
export class CompaniesService {

  BASE_URL = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {
  }

  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.BASE_URL}/api/companies/`);

  }

  getCompanyVacancies(id: number): Observable<CompanyVacancies> {
    return this.http.get<CompanyVacancies>(`${this.BASE_URL}/api/companies/${id}/vacancies/`);
  }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/api/login/`, {
      username,
      password
    });
  }
}
