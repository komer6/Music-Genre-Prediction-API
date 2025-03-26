import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddpredictComponent } from './addpredict.component';

describe('AddpredictComponent', () => {
  let component: AddpredictComponent;
  let fixture: ComponentFixture<AddpredictComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AddpredictComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddpredictComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
