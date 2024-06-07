// Define a function that returns a promise after a delay
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  // Define an async function
  async function asyncFunction() {
    console.log("Start");
  
    // Use await to wait for the promise to resolve
    await delay(2000);
    console.log("After 2 seconds");
  
    await delay(1000);
    console.log("After another second");
  
    return "Done";
  }
  
  // Call the async function
  asyncFunction().then(result => {
    console.log(result); // Output: Done
  }).catch(error => {
    console.error("Error:", error);
  });
  