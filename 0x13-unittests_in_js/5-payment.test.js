const { expect } = require("chai");
const sinon = require('sinon');
const { spy } = require('sinon');

const sendPaymentRequestToApi = require('./3-payment');

describe('hooks', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });

  it('sendPaymentRequestToAPI', () => {
    sendPaymentRequestToApi(100, 20);
    expect(consoleSpy.calledWithExactly('The total is: 120')).to.equal(true);
    expect(consoleSpy.calledOnce).to.equal(true);
  });

  it('sendPaymentRequestToAPI', () => {
    sendPaymentRequestToApi(10, 10);
    expect(consoleSpy.calledWithExactly('The total is: 20')).to.equal(true);
    expect(consoleSpy.calledOnce).to.equal(true);
  });

  afterEach(() => {
    consoleSpy.restore();
  })
});
