// Function to create an n-dimensional array
function createNDArray(dimensions, initialValue = 0) {
    if (dimensions.length === 0) {
        return initialValue;
    }
    const dimension = dimensions[0];
    const restDimensions = dimensions.slice(1);
    
    const array = [];
    for (let i = 0; i < dimension; i++) {
        array.push(createNDArray(restDimensions, initialValue));
    }
    
    return array;
}

// Define dimensions for the 5D array (e.g., 2x2x2x2x2)
const dimensions = [2, 2, 2, 2, 2];

// Create the 5D array with an initial value of 0
const array5D = createNDArray(dimensions);

// Example to set a value in the 5D array
array5D[0][1][1][0][1] = 42;

// Log the 5D array to the console
console.log(JSON.stringify(array5D, null, 2));