import random
import sqlite3
import datetime
import os
import json
from typing import List, Dict, Tuple
import tkinter as tk
from tkinter import messagebox, simpledialog

class Activity:
    def __init__(self, id: int, name: str, category: str, duration: int, cost: float, last_picked: datetime.date = None):
        self.id = id
        self.name = name
        self.category = category
        self.duration = duration  # in minutes
        self.cost = cost  # in dollars
        self.last_picked = last_picked

class ActivityManager:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                duration INTEGER NOT NULL,
                cost REAL NOT NULL,
                last_picked DATE
            )
        ''')
        self.conn.commit()

    def add_activity(self, activity: Activity):
        self.cursor.execute('''
            INSERT INTO activities (name, category, duration, cost, last_picked)
            VALUES (?, ?, ?, ?, ?)
        ''', (activity.name, activity.category, activity.duration, activity.cost, activity.last_picked))
        self.conn.commit()

    def get_all_activities(self) -> List[Activity]:
        self.cursor.execute('SELECT * FROM activities')
        return [Activity(*row) for row in self.cursor.fetchall()]

    def update_last_picked(self, activity_id: int, date: datetime.date):
        self.cursor.execute('UPDATE activities SET last_picked = ? WHERE id = ?', (date, activity_id))
        self.conn.commit()

    def get_activity_by_id(self, activity_id: int) -> Activity:
        self.cursor.execute('SELECT * FROM activities WHERE id = ?', (activity_id,))
        return Activity(*self.cursor.fetchone())

    def close(self):
        self.conn.close()

class ActivityPicker:
    def __init__(self, activity_manager: ActivityManager):
        self.activity_manager = activity_manager

    def pick_random_activity(self, filters: Dict[str, any] = None) -> Activity:
        activities = self.activity_manager.get_all_activities()
        if filters:
            activities = [a for a in activities if self._matches_filters(a, filters)]
        if not activities:
            raise ValueError("No activities match the given filters")
        chosen = random.choice(activities)
        self.activity_manager.update_last_picked(chosen.id, datetime.date.today())
        return chosen

    def _matches_filters(self, activity: Activity, filters: Dict[str, any]) -> bool:
        for key, value in filters.items():
            if key == 'max_duration' and activity.duration > value:
                return False
            if key == 'max_cost' and activity.cost > value:
                return False
            if key == 'category' and activity.category != value:
                return False
        return True

class GUI:
    def __init__(self, picker: ActivityPicker):
        self.picker = picker
        self.root = tk.Tk()
        self.root.title("Quality Time Activity Picker")
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self.root, text="Pick Random Activity", command=self.pick_activity).pack(pady=10)
        tk.Button(self.root, text="Add New Activity", command=self.add_activity).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    def pick_activity(self):
        try:
            filters = self.get_filters()
            activity = self.picker.pick_random_activity(filters)
            messagebox.showinfo("Random Activity", f"Your activity is: {activity.name}\n"
                                                   f"Category: {activity.category}\n"
                                                   f"Duration: {activity.duration} minutes\n"
                                                   f"Cost: ${activity.cost:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def get_filters(self) -> Dict[str, any]:
        filters = {}
        max_duration = simpledialog.askinteger("Filter", "Maximum duration (in minutes, 0 for no limit):", minvalue=0)
        if max_duration:
            filters['max_duration'] = max_duration
        max_cost = simpledialog.askfloat("Filter", "Maximum cost (in dollars, 0 for no limit):", minvalue=0)
        if max_cost:
            filters['max_cost'] = max_cost
        category = simpledialog.askstring("Filter", "Specific category (leave empty for any):")
        if category:
            filters['category'] = category
        return filters

    def add_activity(self):
        name = simpledialog.askstring("New Activity", "Activity name:")
        category = simpledialog.askstring("New Activity", "Category:")
        duration = simpledialog.askinteger("New Activity", "Duration (in minutes):", minvalue=1)
        cost = simpledialog.askfloat("New Activity", "Cost (in dollars):", minvalue=0)
        if all([name, category, duration, cost]):
            new_activity = Activity(None, name, category, duration, cost)
            self.picker.activity_manager.add_activity(new_activity)
            messagebox.showinfo("Success", "New activity added successfully!")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def run(self):
        self.root.mainloop()

def load_initial_activities(file_path: str) -> List[Dict]:
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return []

def main():
    db_path = 'activities.db'
    initial_activities_file = 'initial_activities.json'

    activity_manager = ActivityManager(db_path)
    
    # Load initial activities if the database is empty
    if not activity_manager.get_all_activities():
        initial_activities = load_initial_activities(initial_activities_file)
        for activity_data in initial_activities:
            activity = Activity(None, **activity_data)
            activity_manager.add_activity(activity)

    picker = ActivityPicker(activity_manager)
    gui = GUI(picker)
    gui.run()

    activity_manager.close()

if __name__ == "__main__":
    main()