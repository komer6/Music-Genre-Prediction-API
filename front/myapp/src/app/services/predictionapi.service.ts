import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PredictionapiService {
  MY_SERVER = 'http://127.0.0.1:8000/';  // FastAPI endpoint

  constructor(private myServ: HttpClient) {}

  // Define the method that calls the FastAPI endpoint
  predict(age: number, gender: string): Observable<string> {
    const payload = { age: age, gender: gender };
    return this.myServ.post<string>(this.MY_SERVER+"convert", payload);
  }
  addathing(age: number, gender: string, genre:string): Observable<string> {
    const payload = { age: age, gender: gender, genre:genre};
    return this.myServ.post<string>(this.MY_SERVER+"save_to_csv", payload);
  }
  
}
