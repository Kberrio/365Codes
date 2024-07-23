import java.util.ArrayList;
import java.util.List;

class MenuItem {
    private String name;
    private double price;

    public MenuItem(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }
}

class Order {
    private List<MenuItem> items;

    public Order() {
        this.items = new ArrayList<>();
    }

    public void addItem(MenuItem item) {
        items.add(item);
    }

    public double calculateTotal() {
        return items.stream().mapToDouble(MenuItem::getPrice).sum();
    }

    public void displayOrder() {
        System.out.println("Order details:");
        for (MenuItem item : items) {
            System.out.println(item.getName() + " - $" + item.getPrice());
        }
        System.out.println("Total: $" + calculateTotal());
    }
}

class Restaurant {
    private List<MenuItem> menu;

    public Restaurant() {
        this.menu = new ArrayList<>();
        initializeMenu();
    }

    private void initializeMenu() {
        menu.add(new MenuItem("Burger", 9.99));
        menu.add(new MenuItem("Pizza", 12.99));
        menu.add(new MenuItem("Salad", 7.99));
        menu.add(new MenuItem("Fries", 3.99));
        menu.add(new MenuItem("Soda", 1.99));
    }

    public void displayMenu() {
        System.out.println("Menu:");
        for (int i = 0; i < menu.size(); i++) {
            MenuItem item = menu.get(i);
            System.out.println((i + 1) + ". " + item.getName() + " - $" + item.getPrice());
        }
    }

    public MenuItem getMenuItem(int index) {
        if (index >= 0 && index < menu.size()) {
            return menu.get(index);
        }
        return null;
    }
}

public class RestaurantSystem {
    public static void main(String[] args) {
        Restaurant restaurant = new Restaurant();
        Order order = new Order();

        restaurant.displayMenu();

        // Simulating order placement
        order.addItem(restaurant.getMenuItem(0)); // Adding Burger
        order.addItem(restaurant.getMenuItem(3)s); // Adding Fries
        order.addItem(restaurant.getMenuItem(4)); // Adding Soda

        order.displayOrder();
    }
}