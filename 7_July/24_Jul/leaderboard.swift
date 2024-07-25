struct Player: Identifiable, Comparable {
    let id = UUID()
    let name: String
    var score: Int
    
    static func < (lhs: Player, rhs: Player) -> Bool {
        return lhs.score > rhs.score // Sort in descending order
    }
}

class Leaderboard {
    private var players: [Player] = []
    
    func addPlayer(_ player: Player) {
        players.append(player)
        sortLeaderboard()
    }
    
    func updateScore(for playerName: String, newScore: Int) {
        if let index = players.firstIndex(where: { $0.name == playerName }) {
            players[index].score = newScore
            sortLeaderboard()
        }
    }
    
    func getTopPlayers(_ count: Int) -> [Player] {
        return Array(players.prefix(count))
    }
    
    private func sortLeaderboard() {
        players.sort()
    }
}

// Usage example
let leaderboard = Leaderboard()

leaderboard.addPlayer(Player(name: "Alice", score: 100))
leaderboard.addPlayer(Player(name: "Bob", score: 85))
leaderboard.addPlayer(Player(name: "Charlie", score: 95))

leaderboard.updateScore(for: "Bob", newScore: 110)

let topThree = leaderboard.getTopPlayers(3)
for (index, player) in topThree.enumerated() {
    print("\(index + 1). \(player.name): \(player.score)")
}