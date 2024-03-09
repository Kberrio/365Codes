public class Main {
    public static void main(String[] args) {
        // Create two Pokemon
        Pokemon pikachu = new Pokemon("Pikachu", 100, 30);
        Pokemon charmander = new Pokemon("Charmander", 100, 25);

        // Simulate a battle
        pikachu.attack(charmander);
        charmander.attack(pikachu);
        
        // You can add more logic here to continue the battle, manage turns, etc.
    }
}
