public class Pokemon {
    // Attributes
    private String name;
    private int health;
    private int attackDamage;

    // Constructor
    public Pokemon(String name, int health, int attackDamage) {
        this.name = name;
        this.health = health;
        this.attackDamage = attackDamage;
    }

    // Methods
    public void attack(Pokemon other) {
        System.out.println(this.name + " attacks " + other.getName() + " for " + this.attackDamage + " damage.");
        other.reduceHealth(this.attackDamage);
    }

    public void reduceHealth(int damage) {
        this.health -= damage;
        if (this.health < 0) this.health = 0;
        System.out.println(this.name + " now has " + this.health + " health.");
    }

    // Getters
    public String getName() {
        return name;
    }

    public int getHealth() {
        return health;
    }
}
