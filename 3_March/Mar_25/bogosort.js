// Function to check if an array is sorted
function isSorted(arr) {
    for (let i = 1; i < arr.length; i++) {
        if (arr[i - 1] > arr[i]) {
            return false;
        }
    }
    return true;
}

// Function to shuffle an array randomly
function shuffle(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
}

// Function to perform Bogo Sort
function bogoSort(arr) {
    let attempts = 0;
    while (!isSorted(arr)) {
        shuffle(arr);
        attempts++;
    }
    console.log("Sorted after " + attempts + " attempts.");
    return arr;
}

// Example usage:
const arr = [5, 2, 9, 1, 5, 6];
console.log("Original array:", arr);
console.log("Sorted array:", bogoSort(arr));
