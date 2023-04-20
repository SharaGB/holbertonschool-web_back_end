const getPaymentTokenFromAPI = (success) => {
  if (success) return new Promise((resolve, reject) => {
    resolve({ data: 'Successful response from the API' });
  });
};

module.exports = getPaymentTokenFromAPI;
