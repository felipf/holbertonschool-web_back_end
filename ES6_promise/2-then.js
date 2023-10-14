function handleResponseFromAPI(promise) {
  return new Promise((resolve, reject) => {
    if (promise) {
      console.log("Got a response from the API");
      resolve({ status: 200, body: "Success" });
    } else {
      console.log("Got a response from the API");
      reject(new Error());
    }
  });
}

export default handleResponseFromAPI;