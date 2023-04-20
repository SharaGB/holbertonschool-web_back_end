const calculateNumber = require("./0-calcul.js");
const assert = require("assert");

describe('calculateNumber', () => {
  it('returns rounded positive sum', () => {
    assert.strictEqual(calculateNumber(4, 8), 12);
    assert.strictEqual(calculateNumber(1.9, 0), 2);
    assert.strictEqual(calculateNumber(6.1, 6.1), 12);
    assert.strictEqual(calculateNumber(0.1, 0.2), 0);
    assert.strictEqual(calculateNumber(0.1, 0.6), 1);
  });

  it('returns rounded negative sum', () => {
    assert.strictEqual(calculateNumber(-1, -3), -4);
    assert.strictEqual(calculateNumber(-1.4, -3.6), -5);
  });

  it('returns TypeError', () => {
    assert.throws(() => calculateNumber(NaN, 5.6), { name: 'TypeError' });
    assert.throws(() => calculateNumber(5.6, NaN), { name: 'TypeError' });
    assert.throws(() => calculateNumber(NaN, NaN), { name: 'TypeError' });
  });
});
