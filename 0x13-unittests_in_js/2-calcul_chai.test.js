const calculateNumber = require("./2-calcul_chai.js");
const { expect } = require("chai");

describe('SUM', () => {
  it('returns rounded positive sum', () => {
    expect(calculateNumber('SUM', 4, 8)).to.equal(12);
    expect(calculateNumber('SUM', 1.9, 0)).to.equal(2);
    expect(calculateNumber('SUM', 6.1, 6.1)).to.equal(12);
    expect(calculateNumber('SUM', 0.1, 0.2)).to.equal(0);
    expect(calculateNumber('SUM', 0.1, 0.6)).to.equal(1);
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });

  it('returns rounded negative sum', () => {
    expect(calculateNumber('SUM', -1, -3)).to.equal(-4);
    expect(calculateNumber('SUM', -1.4, -3.6)).to.equal(-5);
  });

  it('returns TypeError', () => {
    expect(() => calculateNumber('SUM', NaN, 5.6)).to.throw(TypeError);
    expect(() => calculateNumber('SUM', 5.6, NaN)).to.throw(TypeError);
    expect(() => calculateNumber('SUM', NaN, NaN)).to.throw(TypeError);
  });
});

describe('SUBTRACT', () => {
  it('returns rounded positive substract', () => {
    expect(calculateNumber('SUBTRACT', 8, 4)).to.equal(4);
    expect(calculateNumber('SUBTRACT', 1.9, 0)).to.equal(2);
    expect(calculateNumber('SUBTRACT', 6.1, 6.1)).to.equal(0);
    expect(calculateNumber('SUBTRACT', 1, 0.2)).to.equal(1);
    expect(calculateNumber('SUBTRACT', 0.6, 0.1)).to.equal(1);
    expect(calculateNumber('SUBTRACT', 4.5, 1.4)).to.equal(4);
  });

  it('returns rounded negative substract', () => {
    expect(calculateNumber('SUBTRACT', -1, -3), 2);
    expect(calculateNumber('SUBTRACT', -1.4, -3.6), 3);
  });

  it('returns TypeError', () => {
    expect(() => calculateNumber('SUBTRACT', NaN, 5.6)).to.throw(TypeError);
    expect(() => calculateNumber('SUBTRACT', 5.6, NaN)).to.throw(TypeError);
    expect(() => calculateNumber('SUBTRACT', NaN, NaN)).to.throw(TypeError);
  });
});

describe('DIVIDE', () => {
  it('returns rounded positive divide', () => {
    expect(calculateNumber('DIVIDE', 8, 4), 2);
    expect(calculateNumber('DIVIDE', 6.1, 1.7), 3);
    expect(calculateNumber('DIVIDE', 6.1, 6.1), 1);
    expect(calculateNumber('DIVIDE', 2.0, 1.1), 2);
    expect(calculateNumber('DIVIDE', 0.6, 0.9), 1);
    expect(calculateNumber('DIVIDE', 4.5, 5), 1);
  });

  it('returns rounded negative divide', () => {
    expect(calculateNumber('DIVIDE', -2, 1.1), -2);
    expect(calculateNumber('DIVIDE', -4.4, -2.2), 2);
  });

  it('returns Error', () => {
    expect(calculateNumber('DIVIDE', 2, 0), 'Error');
    expect(calculateNumber('DIVIDE', 3, 0), 'Error');
    expect(calculateNumber('DIVIDE', 4, 0), 'Error');
  });

  it('returns TypeError', () => {
    expect(() => calculateNumber('DIVIDE', NaN, 5.6)).to.throw(TypeError);
    expect(() => calculateNumber('DIVIDE', 5.6, NaN)).to.throw(TypeError);
    expect(() => calculateNumber('DIVIDE', NaN, NaN)).to.throw(TypeError);
  });
});
