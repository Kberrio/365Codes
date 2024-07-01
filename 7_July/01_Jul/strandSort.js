function strandSort(arr) {
    if (arr.length <= 1) {
      return arr;
    }
  
    let result = [];
  
    while (arr.length > 0) {
      let sublist = [arr.shift()]; // Start sublist with the first element
  
      for (let i = 0; i < arr.length; ) {
        if (arr[i] >= sublist[sublist.length - 1]) {
          sublist.push(arr.splice(i, 1)[0]); // Move elements to sublist if they are in order
        } else {
          i++;
        }
      }
  
      result = merge(result, sublist); // Merge the sublist into the result
    }
  
    return result;
  }
  
  function merge(arr1, arr2) {
    let merged = [];
    let i = 0;
    let j = 0;
  
    while (i < arr1.length && j < arr2.length) {
      if (arr1[i] < arr2[j]) {
        merged.push(arr1[i++]);
      } else {
        merged.push(arr2[j++]);
      }
    }
  
    // Add remaining elements of arr1, if any
    while (i < arr1.length) {
      merged.push(arr1[i++]);
    }
  
    // Add remaining elements of arr2, if any
    while (j < arr2.length) {
      merged.push(arr2[j++]);
    }
  
    return merged;
  }
  
  // Example usage:
  let arr = [4, 2, 3, 1, 5, 9, 7, 8, 6];
  console.log("Original array:", arr);
  let sortedArr = strandSort(arr);
  console.log("Sorted array:", sortedArr);
  