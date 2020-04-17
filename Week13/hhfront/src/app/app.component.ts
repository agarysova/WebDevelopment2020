import {Component, OnInit} from '@angular/core';
import {CompaniesService} from './companies.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'hhFront';

  logged = false;

  username = '';
  password = '';

  constructor(private companiesService: CompaniesService) {}

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }
  login() {
    this.companiesService.login(this.username, this.password)
      .subscribe(res => {
        localStorage.setItem('token', res.token);
        this.logged = true;

        this.username = '';
        this.password = '';
      });
  }
  logout() {
    localStorage.clear();
    this.logged = false;
  }
}
