const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
  it('request /', (done) => {
    request('http://localhost:7865', (error, response, body) => {
      if (response) {
        expect(response.statusCode).to.equal(200);
        expect(response.statusMessage).to.equal('OK');
        expect(body).to.equals('Welcome to the payment system');
        done();
      }
    });
  });

  it('request /cart/:id success', (done) => {
    request('http://localhost:7865/cart/12', (error, response, body) => {
      if (response) {
        expect(response.statusCode).to.equal(200);
        expect(response.statusMessage).to.equal('OK');
        expect(body).to.equals('Payment methods for cart 12');
        done();
      }
    });
  });

  it('request /cart/:id error', (done) => {
    request('http://localhost:7865/cart/hello', (error, response, body) => {
      if (response) {
        expect(response.statusCode).to.equal(404);
        done();
      }
    });
  });

  it('request /available_payments', (done) => {
    request('http://localhost:7865/available_payments', (error, response, body) => {
      if (response) {
        expect(response.statusCode).to.equal(200);
        expect(JSON.parse(body)).to.eql({ payment_methods: { credit_cards: true, paypal: false } });
        done();
      }
    });
  });

  it('request /login success', (done) => {
    request.post({ uri: 'http://localhost:7865/login', method: 'POST', json: { userName: "Betty" } }, (error, response, body) => {
      if (response) {
        expect(response.statusCode).to.equal(200);
        expect(body).equals("Welcome Betty")
        done();
      }
    });
  });

  it('request /login undefined', (done) => {
    request.post({ uri: 'http://localhost:7865/login', method: 'POST' }, (error, response, body) => {
      if (response) {
        expect(response.statusCode).to.equal(200);
        expect(body).equals("Welcome undefined")
        done();
      }
    });
  });
});
