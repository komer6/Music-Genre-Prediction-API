import { TestBed } from '@angular/core/testing';

import { PredictionapiService } from './predictionapi.service';

describe('PredictionapiService', () => {
  let service: PredictionapiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PredictionapiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
