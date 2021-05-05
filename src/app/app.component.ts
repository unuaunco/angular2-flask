import { Component } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  title = 'angular2-flask-builded';

  constructor(
    private translate: TranslateService
  ) {
    this.translate.setDefaultLang('en');
  }
}
