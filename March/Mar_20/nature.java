import java.util.Random;

public class NatureProgram {
    public static void main(String[] args) {
        // Create an array of different types of natural elements
        String[] elements = {"trees", "flowers", "rivers", "mountains", "animals"};

        // Create a random number generator
        Random random = new Random();

        // Select a random element from the array
        String selectedElement = elements[random.nextInt(elements.length)];

        // Display a message about the selected element
        System.out.println("Today, let's learn about " + selectedElement + ":");

        // Switch statement to display information based on the selected element
        switch (selectedElement) {
            case "trees":
                System.out.println("Trees are vital to our planet as they provide oxygen, store carbon, and provide habitats for animals.");
                break;
            case "flowers":
                System.out.println("Flowers come in various colors, shapes, and sizes, and play a crucial role in pollination and beautifying our environment.");
                break;
            case "rivers":
                System.out.println("Rivers are bodies of flowing water that are essential for providing drinking water, irrigation, transportation, and habitat for many species.");
                break;
            case "mountains":
                System.out.println("Mountains are majestic landforms that provide biodiversity hotspots, fresh water, and recreational opportunities for humans.");
                break;
            case "animals":
                System.out.println("Animals are diverse creatures that inhabit various ecosystems, playing roles as predators, prey, pollinators, and seed dispersers.");
                break;
            default:
                System.out.println("Sorry, we couldn't find information about this element.");
        }
    }
}
