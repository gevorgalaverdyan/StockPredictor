import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';



@Injectable({
  providedIn: 'root',
})
export class PredictionService {
  constructor(private http: HttpClient) {}

  getPredictions():  Observable<any>{
    return of({message: "Predictions"});
  }
}
