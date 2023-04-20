const { expect } = require('chai');
const sinon = require('sinon');
const { spy } = require('sinon');

const sendPaymentRequestToApi = require('./3-payment');
const utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('sendPaymentRequestToApi(100, 20) is the same Utils.calculateNumber(\'SUM\', 100, 20)', () => {
    const functionSpy = sinon.spy(utils, 'calculateNumber');
    const consoleSpy = sinon.spy(console, 'log');

    const apiRequest = sendPaymentRequestToApi(100, 20);

    expect(functionSpy.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
    expect(consoleSpy.calledWithExactly('The total is: 120')).to.equal(true);
    expect(utils.calculateNumber('SUM', 100, 20)).to.equal(apiRequest);

    functionSpy.restore();
    consoleSpy.restore();
  });
});
