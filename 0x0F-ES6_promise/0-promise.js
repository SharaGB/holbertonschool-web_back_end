/* promise need a function to work */
function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
        if (true) {
            resolve();
        } else {
            reject();
        }
    });
}

export default getResponseFromAPI;