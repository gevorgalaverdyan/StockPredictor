import { Component, OnInit } from '@angular/core';
import { PredictionService } from './services/prediction.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  constructor(private predictionService: PredictionService) { }

  ngOnInit(): void {
    this.predictionService.getPredictions().subscribe((data: any) => {
      console.log(data);
    });
  }
}
