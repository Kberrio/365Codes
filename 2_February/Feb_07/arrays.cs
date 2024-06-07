using System;

class Program
{
    static void Main(string[] args)
    {
        // Define an array of integers
        int[] numbers = { 1, 2, 3, 4, 5 };

        // Print the original array
        Console.WriteLine("Original array:");
        foreach (int num in numbers)
        {
            Console.Write(num + " ");
        }
        Console.WriteLine();

        // Multiply each element of the array by 2
        Console.WriteLine("Array after multiplying each element by 2:");
        for (int i = 0; i < numbers.Length; i++)
        {
            numbers[i] *= 2;
        }

        // Print the modified array
        foreach (int num in numbers)
        {
            Console.Write(num + " ");
        }
        Console.WriteLine();

        // Calculate the sum of elements in the array
        int sum = 0;
        foreach (int num in numbers)
        {
            sum += num;
        }
        Console.WriteLine("Sum of elements in the array: " + sum);
    }
}
