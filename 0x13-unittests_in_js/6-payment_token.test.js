const { expect } = require("chai");

const getPaymentTokenFromAPI = require('./6-payment_token')

describe('getPaymentTokenFromAPI', () => {
  it('getPaymentTokenFromAPI(true)', (done) => {
    getPaymentTokenFromAPI(true).then((response) => {
      expect(response).to.eql({ data: 'Successful response from the API' })
      done();
    }).catch((err) => {
      done(err);
    });
  });
});
