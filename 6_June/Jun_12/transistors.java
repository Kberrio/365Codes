public class Transistor {
    // Properties of the transistor
    private String type; // Type of transistor (e.g., NPN, PNP)
    private double gain; // Current gain (hFE)
    private double voltage; // Operating voltage

    // Constructor to initialize the transistor
    public Transistor(String type, double gain, double voltage) {
        this.type = type;
        this.gain = gain;
        this.voltage = voltage;
    }

    // Getter methods to access the properties
    public String getType() {
        return type;
    }

    public double getGain() {
        return gain;
    }

    public double getVoltage() {
        return voltage;
    }

    // Method to display the transistor details
    public void displayDetails() {
        System.out.println("Transistor Details:");
        System.out.println("Type: " + type);
        System.out.println("Gain (hFE): " + gain);
        System.out.println("Voltage: " + voltage + "V");
    }

    public static void main(String[] args) {
        // Create an instance of the Transistor class
        Transistor transistor = new Transistor("NPN", 100, 5.0);

        // Display the details of the transistor
        transistor.displayDetails();
    }
}
