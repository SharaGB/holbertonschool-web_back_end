const calculateNumber = (a, b) => {
  if (isNaN(a) || isNaN(b))
    throw new TypeError();
  return Math.round(a) + Math.round(b);
};

module.exports = calculateNumber;
