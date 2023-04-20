const { expect } = require('chai');
const sinon = require('sinon');
const { stub, spy } = require('sinon');

const sendPaymentRequestToApi = require('./3-payment');
const utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('Utils.calculateNumber', () => {
    const functionStub = sinon.stub(utils, 'calculateNumber');
    functionStub.returns(10)
    const consoleSpy = sinon.spy(console, 'log');

    const apiRequest = sendPaymentRequestToApi(100, 20);

    expect(functionStub.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
    expect(consoleSpy.calledWithExactly('The total is: 10')).to.equal(true);
    expect(utils.calculateNumber('SUM', 100, 20)).to.equal(apiRequest);

    functionStub.restore();
    consoleSpy.restore();
  });
});
