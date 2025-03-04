# main.py - Application entry point
import tkinter as tk
from tkinter import ttk
from frames.home_frame import HomeFrame
from frames.exercise_frame import ExerciseFrame
from frames.workout_frame import WorkoutFrame
from frames.history_frame import HistoryFrame
from frames.stats_frame import StatsFrame
from database.db_manager import DatabaseManager

class WorkoutTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configure main window
        self.title("Workout Tracker")
        self.geometry("800x600")
        self.minsize(800, 600)
        
        # Initialize database
        self.db_manager = DatabaseManager("workout_data.db")
        
        # Set up navigation
        self.setup_navigation()
        
        # Configure frame container
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        
        # Initialize frames
        self.frames = {}
        self.setup_frames()
        
        # Show home frame by default
        self.show_frame("HomeFrame")
    
    def setup_navigation(self):
        # Navigation bar
        nav_bar = tk.Frame(self, bg="#333333")
        nav_bar.pack(side="top", fill="x")
        
        # Navigation buttons
        buttons = [
            ("Home", lambda: self.show_frame("HomeFrame")),
            ("Exercises", lambda: self.show_frame("ExerciseFrame")),
            ("Workouts", lambda: self.show_frame("WorkoutFrame")),
            ("History", lambda: self.show_frame("HistoryFrame")),
            ("Statistics", lambda: self.show_frame("StatsFrame"))
        ]
        
        for text, command in buttons:
            button = tk.Button(nav_bar, text=text, command=command, 
                               bg="#333333", fg="white", bd=0, padx=15, pady=8)
            button.pack(side="left")
    
    def setup_frames(self):
        # Create and store all application frames
        frame_classes = [
            HomeFrame,
            ExerciseFrame,
            WorkoutFrame,
            HistoryFrame,
            StatsFrame
        ]
        
        for F in frame_classes:
            frame_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
    
    def show_frame(self, frame_name):
        # Raise the requested frame to the top
        frame = self.frames.get(frame_name)
        if frame:
            frame.tkraise()

if __name__ == "__main__":
    app = WorkoutTrackerApp()
    app.mainloop()
