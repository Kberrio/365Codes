#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

struct Player {
    std::string name;
    int score;
};

bool compareScores(const Player& a, const Player& b) {
    return a.score > b.score;
}

class Leaderboard {
private:
    std::vector<Player> players;

public:
    void addPlayer(const std::string& name, int score) {
        players.push_back({name, score});
        std::sort(players.begin(), players.end(), compareScores);
    }

    void displayLeaderboard() {
        std::cout << "Leaderboard:\n";
        for (size_t i = 0; i < players.size(); ++i) {
            std::cout << i + 1 << ". " << players[i].name << " - " << players[i].score << " points\n";
        }
    }
};

int main() {
    Leaderboard leaderboard;

    leaderboard.addPlayer("Alice", 100);
    leaderboard.addPlayer("Bob", 85);
    leaderboard.addPlayer("Charlie", 95);
    leaderboard.addPlayer("David", 110);

    leaderboard.displayLeaderboard();

    return 0;
}