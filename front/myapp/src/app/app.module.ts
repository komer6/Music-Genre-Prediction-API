import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { MatSelectModule } from '@angular/material/select';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatOptionModule } from '@angular/material/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PredictComponent } from './components/predict/predict.component';
import { AddpredictComponent } from './components/addpredict/addpredict.component';

@NgModule({
  declarations: [
    AppComponent,
    PredictComponent,
    AddpredictComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
     MatInputModule,
    MatSelectModule,
    MatOptionModule,
    HttpClientModule

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
