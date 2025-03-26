import { Component } from '@angular/core';
import { PredictionapiService } from '../../services/predictionapi.service';

@Component({
  selector: 'app-addpredict',
  standalone: false,
  templateUrl: './addpredict.component.html',
  styleUrl: './addpredict.component.css'
})
export class AddpredictComponent {
    predictionResult: string = '';  // To store the prediction result
  
    constructor(private predictionApiService: PredictionapiService) {}
  
    // Ensure the getPrediction method accepts 'age' and 'gender' as arguments
    addst(age: string, gender: string, gnere:string) {
      if (age && gender && gnere) {
        this.predictionApiService.addathing(Number(age), gender,gnere).subscribe(
          (result: string) => {
            this.predictionResult = result;
            console.log(this.predictionResult);
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


