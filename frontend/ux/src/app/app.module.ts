import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { StockChartComponent } from './components/stock-chart/stock-chart.component';
import { UserInputSidebarComponent } from './components/user-input-sidebar/user-input-sidebar.component';

@NgModule({
  declarations: [
    AppComponent,
    StockChartComponent,
    UserInputSidebarComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
