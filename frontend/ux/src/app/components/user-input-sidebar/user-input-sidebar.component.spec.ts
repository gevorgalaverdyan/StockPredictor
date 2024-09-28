import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UserInputSidebarComponent } from './user-input-sidebar.component';

describe('UserInputSidebarComponent', () => {
  let component: UserInputSidebarComponent;
  let fixture: ComponentFixture<UserInputSidebarComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [UserInputSidebarComponent]
    });
    fixture = TestBed.createComponent(UserInputSidebarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
