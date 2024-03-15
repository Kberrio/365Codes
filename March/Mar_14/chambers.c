#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define CHAMBERS 6

int main() {
    int chambers[CHAMBERS];
    int bulletPosition;
    int playerChoice;
    int playerWins = 0;
    int rounds = 0;

    srand(time(NULL));

    printf("Welcome to the deadly game of Russian Roulette!\n\n");

    do {
        // Load a single bullet into a random chamber
        bulletPosition = rand() % CHAMBERS;
        for (int i = 0; i < CHAMBERS; i++) {
            if (i == bulletPosition) {
                chambers[i] = 1; // Bullet loaded
            } else {
                chambers[i] = 0; // Empty chamber
            }
        }

        // Player chooses a chamber
        printf("Pick a chamber (1 to %d): ", CHAMBERS);
        scanf("%d", &playerChoice);

        if (playerChoice < 1 || playerChoice > CHAMBERS) {
            printf("Invalid choice. Game over!\n");
            break;
        }

        // Spin the revolver
        int firedChamber = rand() % CHAMBERS;

        // Check if the player survives
        if (firedChamber == bulletPosition) {
            printf("\n*** BANG! You're dead! ***\n\n");
            printf("You survived %d rounds.\n", rounds);
            break;
        } else {
            printf("\n*click*\n\n");
            printf("You survived this round!\n\n");
            playerWins++;
        }

        rounds++;

    } while (1);

    printf("You won %d game(s).\n", playerWins);

    return 0;
}
