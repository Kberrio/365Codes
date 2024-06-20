// Sneakers.java
public class Sneakers {
    // Attributes of the Sneakers class
    private String brand;
    private double size;
    private String color;
    private double price;

    // Constructor to initialize the Sneakers object
    public Sneakers(String brand, double size, String color, double price) {
        this.brand = brand;
        this.size = size;
        this.color = color;
        this.price = price;
    }

    // Method to display the details of the sneakers
    public void displayDetails() {
        System.out.println("Sneakers Details:");
        System.out.println("Brand: " + brand);
        System.out.println("Size: " + size);
        System.out.println("Color: " + color);
        System.out.println("Price: $" + price);
    }

    // Method to apply a discount to the price
    public void applyDiscount(double discountPercentage) {
        if (discountPercentage > 0 && discountPercentage <= 100) {
            price -= price * (discountPercentage / 100);
        } else {
            System.out.println("Invalid discount percentage. Please enter a value between 0 and 100.");
        }
    }

    // Main method to demonstrate the Sneakers class
    public static void main(String[] args) {
        // Creating a Sneakers object
        Sneakers mySneakers = new Sneakers("Nike", 10.5, "Black", 120.00);

        // Displaying the initial details of the sneakers
        mySneakers.displayDetails();

        // Applying a discount to the sneakers
        mySneakers.applyDiscount(20);

        // Displaying the details of the sneakers after the discount
        mySneakers.displayDetails();
    }
}
