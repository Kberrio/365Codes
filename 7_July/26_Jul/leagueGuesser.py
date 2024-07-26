import tkinter as tk
from tkinter import messagebox
import random

class LeagueGuesserGame:
    def __init__(self, master):
        self.master = master
        self.master.title("League Guesser Game")
        self.master.geometry("400x300")

        self.leagues = {
            "Premier League": ["Manchester United", "Liverpool", "Chelsea", "Arsenal"],
            "La Liga": ["Real Madrid", "Barcelona", "Atletico Madrid", "Sevilla"],
            "Bundesliga": ["Bayern Munich", "Borussia Dortmund", "RB Leipzig", "Bayer Leverkusen"],
            "Serie A": ["Juventus", "Inter Milan", "AC Milan", "Napoli"]
        }

        self.current_league = ""
        self.current_team = ""

        self.label = tk.Label(master, text="Guess the league of the following team:", font=("Arial", 14))
        self.label.pack(pady=20)

        self.team_label = tk.Label(master, text="", font=("Arial", 16, "bold"))
        self.team_label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.next_button = tk.Button(master, text="Next Team", command=self.next_team)
        self.next_button.pack(pady=10)

        self.next_team()

    def next_team(self):
        self.current_league = random.choice(list(self.leagues.keys()))
        self.current_team = random.choice(self.leagues[self.current_league])
        self.team_label.config(text=self.current_team)
        self.entry.delete(0, tk.END)

    def check_guess(self):
        guess = self.entry.get().strip().lower()
        correct_league = self.current_league.lower()

        if guess == correct_league:
            messagebox.showinfo("Correct!", f"Well done! {self.current_team} plays in the {self.current_league}.")
        else:
            messagebox.showerror("Incorrect", f"Sorry, that's wrong. {self.current_team} plays in the {self.current_league}.")

        self.next_team()

if __name__ == "__main__":
    root = tk.Tk()
    game = LeagueGuesserGame(root)
    root.mainloop()