import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class Champion {
    String name;
    int height; // Height in centimeters

    Champion(String name, int height) {
        this.name = name;
        this.height = height;
    }

    @Override
    public String toString() {
        return name + " (" + height + " cm)";
    }
}

public class Main {
    public static void main(String[] args) {
        List<Champion> champions = new ArrayList<>();
        
        // Add some champions with their heights
        champions.add(new Champion("Aatrox", 330));
        champions.add(new Champion("Annie", 130));
        champions.add(new Champion("Braum", 240));
        champions.add(new Champion("Cho'Gath", 610));
        champions.add(new Champion("Fizz", 100));
        champions.add(new Champion("Garen", 205));
        champions.add(new Champion("Jinx", 167));
        champions.add(new Champion("Malphite", 730));
        champions.add(new Champion("Teemo", 90));
        champions.add(new Champion("Zac", 240));

        // Sort the list based on height
        Collections.sort(champions, new Comparator<Champion>() {
            @Override
            public int compare(Champion c1, Champion c2) {
                return Integer.compare(c1.height, c2.height);
            }
        });

        // Print the sorted list
        for (Champion champion : champions) {
            System.out.println(champion);
        }
    }
}
