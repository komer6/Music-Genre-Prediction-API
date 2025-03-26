import { Component } from '@angular/core';
import { PredictionapiService } from '../../services/predictionapi.service';

@Component({
  selector: 'app-predict',
  standalone: false,
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.css']
})
export class PredictComponent {
  predictionResult: string = '';  // To store the prediction result

  constructor(private predictionApiService: PredictionapiService) {}

  // Ensure the getPrediction method accepts 'age' and 'gender' as arguments
  getPrediction(age: string, gender: string) {
    if (age && gender) {
      this.predictionApiService.predict(Number(age), gender).subscribe(
        (result: string) => {
          this.predictionResult = result;  // Store the result in a variable
        },
        (error) => {
          console.error('Prediction error:', error);  // Handle any error from the API
        }
      );
    } else {
      console.log('Please provide both age and gender');
    }
  }
}
