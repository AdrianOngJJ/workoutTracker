# frames/home_frame.py
import tkinter as tk
from tkinter import ttk

class HomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Welcome message
        welcome_label = tk.Label(self, text="Welcome to Workout Tracker", font=("Arial", 24))
        welcome_label.pack(pady=20)
        
        # Quick actions frame
        actions_frame = tk.Frame(self)
        actions_frame.pack(pady=20)
        
        # Quick action buttons
        start_workout_btn = tk.Button(actions_frame, text="Start Workout", 
                                     command=self.start_workout, padx=20, pady=10)
        start_workout_btn.grid(row=0, column=0, padx=10, pady=10)
        
        create_workout_btn = tk.Button(actions_frame, text="Create Workout", 
                                     command=lambda: controller.show_frame("WorkoutFrame"), 
                                     padx=20, pady=10)
        create_workout_btn.grid(row=0, column=1, padx=10, pady=10)
        
        view_stats_btn = tk.Button(actions_frame, text="View Statistics", 
                                  command=lambda: controller.show_frame("StatsFrame"), 
                                  padx=20, pady=10)
        view_stats_btn.grid(row=0, column=2, padx=10, pady=10)
        
        # Recent workouts section
        recent_label = tk.Label(self, text="Recent Workouts", font=("Arial", 18))
        recent_label.pack(pady=10)
        
        # Placeholder for recent workouts list
        recent_workouts = ttk.Treeview(self, columns=("Date", "Workout", "Duration"), 
                                     show="headings", height=5)
        recent_workouts.heading("Date", text="Date")
        recent_workouts.heading("Workout", text="Workout")
        recent_workouts.heading("Duration", text="Duration")
        recent_workouts.pack(fill="x", padx=20)
        
        # You would populate this with actual data from your database
    
    def start_workout(self):
        # This would open a dialog to select a workout and start it
        pass

# frames/exercise_frame.py
import tkinter as tk
from tkinter import ttk

class ExerciseFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Header
        header = tk.Label(self, text="Exercise Library", font=("Arial", 20))
        header.pack(pady=10)
        
        # Search and filter controls
        search_frame = tk.Frame(self)
        search_frame.pack(fill="x", padx=20, pady=10)
        
        search_label = tk.Label(search_frame, text="Search:")
        search_label.pack(side="left", padx=5)
        
        search_entry = tk.Entry(search_frame, width=30)
        search_entry.pack(side="left", padx=5)
        
        search_button = tk.Button(search_frame, text="Search", command=self.search_exercises)
        search_button.pack(side="left", padx=5)
        
        # Exercise list
        exercise_frame = tk.Frame(self)
        exercise_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Columns: Name, Muscle Group, Equipment
        self.exercise_tree = ttk.Treeview(exercise_frame, 
                                        columns=("name", "muscle", "equipment"), 
                                        show="headings", 
                                        height=15)
        
        self.exercise_tree.heading("name", text="Exercise Name")
        self.exercise_tree.heading("muscle", text="Muscle Group")
        self.exercise_tree.heading("equipment", text="Equipment")
        
        self.exercise_tree.column("name", width=200)
        self.exercise_tree.column("muscle", width=150)
        self.exercise_tree.column("equipment", width=150)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(exercise_frame, orient="vertical", command=self.exercise_tree.yview)
        self.exercise_tree.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        self.exercise_tree.pack(side="left", fill="both", expand=True)
        
        # Buttons for adding/editing exercises
        button_frame = tk.Frame(self)
        button_frame.pack(fill="x", padx=20, pady=10)
        
        add_button = tk.Button(button_frame, text="Add Exercise", command=self.add_exercise)
        add_button.pack(side="left", padx=5)
        
        edit_button = tk.Button(button_frame, text="Edit Exercise", command=self.edit_exercise)
        edit_button.pack(side="left", padx=5)
        
        delete_button = tk.Button(button_frame, text="Delete Exercise", command=self.delete_exercise)
        delete_button.pack(side="left", padx=5)
        
        # Populate with sample data initially (you'd replace this with database calls)
        self.load_exercises()
    
    def load_exercises(self):
        # Clear existing items
        for item in self.exercise_tree.get_children():
            self.exercise_tree.delete(item)
        
        # Sample data - replace with database call
        sample_exercises = [
            ("Bench Press", "Chest", "Barbell"),
            ("Squat", "Legs", "Barbell"),
            ("Pull-up", "Back", "Body weight"),
            ("Shoulder Press", "Shoulders", "Dumbbells")
        ]
        
        for exercise in sample_exercises:
            self.exercise_tree.insert("", "end", values=exercise)
    
    def search_exercises(self):
        # Implement search functionality
        pass
    
    def add_exercise(self):
        # Open dialog to add new exercise
        pass
    
    def edit_exercise(self):
        # Open dialog to edit selected exercise
        pass
    
    def delete_exercise(self):
        # Delete selected exercise
        pass

# frames/workout_frame.py - Template for workout creation and management
# frames/history_frame.py - Template for workout history
# frames/stats_frame.py - Template for statistics and progress tracking
