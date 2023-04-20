import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';
const kue = require('kue');

const queue = kue.createQueue();
const listJobs = [
  { phoneNumber: '0001', message: 'Message_1'},
  { phoneNumber: '0002', message: 'Message_2'},
  { phoneNumber: '0003', message: 'Message_3'},
  { phoneNumber: '0004', message: 'Message_4'},
  { phoneNumber: '0005', message: 'Message_5'},
  { phoneNumber: '0006', message: 'Message_6'},
];


before(() => {
  queue.testMode.enter();
});

afterEach(() => {
  queue.testMode.clear();
});

after(() => {
  queue.testMode.exit()
});

describe('createPushNotificationsJobs', () => {
  it('Valid Data', () => {
    createPushNotificationsJobs(listJobs, queue);
    expect(queue.testMode.jobs.length).to.equal(6);
    createPushNotificationsJobs(listJobs, queue);
    expect(queue.testMode.jobs.length).to.equal(12);
  });

  it('Invalid Data', () => {
    expect(() => createPushNotificationsJobs('', queue)).to.throw(Error);
    expect(() => createPushNotificationsJobs(123, queue)).to.throw(Error);
    expect(() => createPushNotificationsJobs({id: 120}, queue)).to.throw(Error);
    expect(() => createPushNotificationsJobs(NaN, queue)).to.throw(Error);
  });
});
