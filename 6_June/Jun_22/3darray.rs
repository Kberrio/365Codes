fn main() {
    // Define the dimensions of the 3D array
    let x = 3;
    let y = 3;
    let z = 3;

    // Initialize the 3D array with some values
    let mut array = vec![vec![vec![0; z]; y]; x];

    // Fill the array with some values
    for i in 0..x {
        for j in 0..y {
            for k in 0..z {
                array[i][j][k] = i * 100 + j * 10 + k;
            }
        }
    }

    // Print the values in the 3D array
    for i in 0..x {
        for j in 0..y {
            for k in 0..z {
                println!("array[{}][{}][{}] = {}", i, j, k, array[i][j][k]);
            }
        }
    }
}
