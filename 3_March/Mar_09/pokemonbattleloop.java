import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> pikachuAttacks = new HashMap<>();
        pikachuAttacks.put("Thunder Shock", 30);
        pikachuAttacks.put("Quick Attack", 20);

        Map<String, Integer> charmanderAttacks = new HashMap<>();
        charmanderAttacks.put("Ember", 25);
        charmanderAttacks.put("Scratch", 20);

        Pokemon pikachu = new Pokemon("Pikachu", 100, PokemonType.ELECTRIC, pikachuAttacks);
        Pokemon charmander = new Pokemon("Charmander", 100, PokemonType.FIRE, charmanderAttacks);

        // Example battle loop
        while (pikachu.getHealth() > 0 && charmander.getHealth() > 0) {
            pikachu.attack(charmander, "Thunder Shock");
            if (charmander.getHealth() > 0) {
                charmander.attack(pikachu, "Ember");
            }
        }
    }
}
