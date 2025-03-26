import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddpredictComponent } from './components/addpredict/addpredict.component';
import { PredictComponent } from './components/predict/predict.component';

const routes: Routes = [
{path:'addprediction',component:AddpredictComponent},
{path:'prediction',component:PredictComponent},


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
