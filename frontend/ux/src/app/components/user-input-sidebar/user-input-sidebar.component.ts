import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-user-input-sidebar',
  templateUrl: './user-input-sidebar.component.html',
  styleUrls: ['./user-input-sidebar.component.css']
})
export class UserInputSidebarComponent {
  @Input() stockName: string = "";
  @Input() predictionRange: string = "";
  @Output() onGetPrediction = new EventEmitter();

  onSubmit(){
    if (!this.stockName || !this.predictionRange) {
      alert('Missing info')
      return;
    }

    const prediction = {
      stockName: this.stockName,
      predictionRange: this.predictionRange,
    }

    this.onGetPrediction.emit(prediction);

    this.stockName = '';
    this.predictionRange = '';
  }
}
