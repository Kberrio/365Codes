using System;
using System.Collections.Generic;
using System.Linq;

class Player
{
    public string Name { get; set; }
    public int Score { get; set; }
}

class Leaderboard
{
    private List<Player> players = new List<Player>();

    public void AddPlayer(string name, int score)
    {
        players.Add(new Player { Name = name, Score = score });
        players = players.OrderByDescending(p => p.Score).ToList();
    }

    public void DisplayLeaderboard()
    {
        Console.WriteLine("Leaderboard:");
        for (int i = 0; i < players.Count; i++)
        {
            Console.WriteLine($"{i + 1}. {players[i].Name} - {players[i].Score} points");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Leaderboard leaderboard = new Leaderboard();

        leaderboard.AddPlayer("Alice", 100);
        leaderboard.AddPlayer("Bob", 85);
        leaderboard.AddPlayer("Charlie", 95);
        leaderboard.AddPlayer("David", 110);

        leaderboard.DisplayLeaderboard();
    }
}