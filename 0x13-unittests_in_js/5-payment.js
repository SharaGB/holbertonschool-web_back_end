const { util } = require("chai");
const Utils = require("./utils.js");

const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
  const res = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${res}`);
  return res;
};

module.exports = sendPaymentRequestToApi;
