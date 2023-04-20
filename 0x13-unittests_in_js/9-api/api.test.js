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
});
