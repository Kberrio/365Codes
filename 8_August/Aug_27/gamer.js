const readline = require('readline');

class TextAdventureGame {
    constructor() {
        this.playerHealth = 100;
        this.playerGold = 0;
        this.enemies = ["Goblin", "Orc", "Troll", "Dragon"];
        this.locations = ["Forest", "Cave", "Castle", "Mountain"];
        this.rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
    }

    async startGame() {
        console.log("Welcome to the Text Adventure Game!");
        console.log("You are a brave adventurer seeking fortune and glory.");
        
        while (this.playerHealth > 0) {
            await this.takeTurn();
        }
        
        console.log("Game Over! You have been defeated.");
        console.log(`You collected ${this.playerGold} gold during your adventure.`);
        this.rl.close();
    }

    async takeTurn() {
        const location = this.locations[Math.floor(Math.random() * this.locations.length)];
        console.log(`\nYou find yourself in a ${location}.`);
        
        const choice = await this.askQuestion("Do you want to [e]xplore or [r]est? ");
        
        if (choice.toLowerCase() === 'e') {
            await this.explore();
        } else if (choice.toLowerCase() === 'r') {
            this.rest();
        } else {
            console.log("Invalid choice. You stumble around and lose 5 health.");
            this.playerHealth -= 5;
        }
    }

    async explore() {
        if (Math.random() < 0.7) {  // 70% chance of encounter
            const enemy = this.enemies[Math.floor(Math.random() * this.enemies.length)];
            console.log(`You encounter a ${enemy}!`);
            
            const choice = await this.askQuestion("Do you want to [f]ight or [r]un? ");
            
            if (choice.toLowerCase() === 'f') {
                this.fight(enemy);
            } else if (choice.toLowerCase() === 'r') {
                this.run();
            } else {
                console.log("Invalid choice. You're caught off guard and lose 10 health.");
                this.playerHealth -= 10;
            }
        } else {
            const goldFound = Math.floor(Math.random() * 41) + 10;  // 10 to 50 gold
            this.playerGold += goldFound;
            console.log(`You found ${goldFound} gold!`);
        }
    }

    fight(enemy) {
        const enemyStrength = this.enemies.indexOf(enemy) * 10 + 10;
        const damageTaken = Math.floor(Math.random() * (enemyStrength + 1));
        this.playerHealth -= damageTaken;
        
        const goldWon = Math.floor(Math.random() * (enemyStrength + 1)) + enemyStrength;
        this.playerGold += goldWon;
        
        console.log(`You defeated the ${enemy}!`);
        console.log(`You took ${damageTaken} damage and won ${goldWon} gold.`);
        console.log(`Your health: ${this.playerHealth}`);
    }

    run() {
        const escapeChance = Math.random();
        if (escapeChance > 0.5) {
            console.log("You managed to escape!");
        } else {
            const damageTaken = Math.floor(Math.random() * 11) + 5;  // 5 to 15 damage
            this.playerHealth -= damageTaken;
            console.log(`You couldn't escape and took ${damageTaken} damage while running.`);
            console.log(`Your health: ${this.playerHealth}`);
        }
    }

    rest() {
        const healthGained = Math.floor(Math.random() * 11) + 5;  // 5 to 15 health
        this.playerHealth = Math.min(100, this.playerHealth + healthGained);
        console.log(`You rest and recover ${healthGained} health.`);
        console.log(`Your health: ${this.playerHealth}`);
    }

    askQuestion(question) {
        return new Promise((resolve) => {
            this.rl.question(question, (answer) => {
                resolve(answer);
            });
        });
    }
}

const game = new TextAdventureGame();
game.startGame();