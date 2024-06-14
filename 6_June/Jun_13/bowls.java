import java.util.ArrayList;
import java.util.Scanner;

class Bowl {
    private String name;
    private String size;
    private String color;

    public Bowl(String name, String size, String color) {
        this.name = name;
        this.size = size;
        this.color = color;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "Bowl{" +
                "name='" + name + '\'' +
                ", size='" + size + '\'' +
                ", color='" + color + '\'' +
                '}';
    }
}

public class BowlManager {
    private ArrayList<Bowl> bowls = new ArrayList<>();

    public void addBowl(String name, String size, String color) {
        bowls.add(new Bowl(name, size, color));
    }

    public void listBowls() {
        if (bowls.isEmpty()) {
            System.out.println("No bowls available.");
        } else {
            for (Bowl bowl : bowls) {
                System.out.println(bowl);
            }
        }
    }

    public void findBowlByName(String name) {
        for (Bowl bowl : bowls) {
            if (bowl.getName().equalsIgnoreCase(name)) {
                System.out.println(bowl);
                return;
            }
        }
        System.out.println("Bowl with name " + name + " not found.");
    }

    public static void main(String[] args) {
        BowlManager manager = new BowlManager();
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("1. Add Bowl");
            System.out.println("2. List Bowls");
            System.out.println("3. Find Bowl by Name");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine();  // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter bowl name: ");
                    String name = scanner.nextLine();
                    System.out.print("Enter bowl size: ");
                    String size = scanner.nextLine();
                    System.out.print("Enter bowl color: ");
                    String color = scanner.nextLine();
                    manager.addBowl(name, size, color);
                    break;
                case 2:
                    manager.listBowls();
                    break;
                case 3:
                    System.out.print("Enter bowl name to find: ");
                    String searchName = scanner.nextLine();
                    manager.findBowlByName(searchName);
                    break;
                case 4:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
