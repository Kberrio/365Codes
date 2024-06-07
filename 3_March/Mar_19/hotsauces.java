public class HotSauce {
    // Instance variables
    private String brand;
    private double scovilleScale; // Measured in SHU (Scoville Heat Units)
    private String flavor;

    // Constructor
    public HotSauce(String brand, double scovilleScale, String flavor) {
        this.brand = brand;
        this.scovilleScale = scovilleScale;
        this.flavor = flavor;
    }

    // Getter methods
    public String getBrand() {
        return brand;
    }

    public double getScovilleScale() {
        return scovilleScale;
    }

    public String getFlavor() {
        return flavor;
    }

    // Setter methods
    public void setBrand(String brand) {
        this.brand = brand;
    }

    public void setScovilleScale(double scovilleScale) {
        this.scovilleScale = scovilleScale;
    }

    public void setFlavor(String flavor) {
        this.flavor = flavor;
    }

    // Method to display information about the hot sauce
    public void displayInfo() {
        System.out.println("Brand: " + brand);
        System.out.println("Scoville Scale: " + scovilleScale + " SHU");
        System.out.println("Flavor: " + flavor);
    }

    // Main method to test the HotSauce class
    public static void main(String[] args) {
        // Creating an instance of HotSauce
        HotSauce sriracha = new HotSauce("Sriracha", 2200, "Garlic and Chili");
        
        // Displaying information about the hot sauce
        sriracha.displayInfo();
    }
}
