function permute(array) {
    // Base case: if the array has only one element, return it as the only permutation
    if (array.length === 1) {
        return [array];
    }

    const permutations = [];

    // Iterate over each element in the array
    for (let i = 0; i < array.length; i++) {
        // Clone the array without the current element
        const rest = array.slice(0, i).concat(array.slice(i + 1));

        // Recursively find permutations of the rest of the array
        const restPermutations = permute(rest);

        // Append the current element to each permutation of the rest of the array
        for (const permutation of restPermutations) {
            permutations.push([array[i], ...permutation]);
        }
    }

    return permutations;
}

// Test the permute function
const inputArray = [1, 2, 3];
const result = permute(inputArray);
console.log("Permutations:", result);
