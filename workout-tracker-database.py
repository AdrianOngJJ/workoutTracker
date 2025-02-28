# database/db_manager.py
import sqlite3
import os
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_file):
        """Initialize database connection and create tables if they don't exist"""
        # Check if database file exists
        db_exists = os.path.exists(db_file)
        
        # Connect to database (creates file if it doesn't exist)
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        
        # Create tables if database is new
        if not db_exists:
            self.create_tables()
    
    def create_tables(self):
        """Create the database schema"""
        # Exercise table
        self.cursor.execute('''
        CREATE TABLE exercises (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            muscle_group TEXT NOT NULL,
            equipment TEXT,
            description TEXT
        )
        ''')
        
        # Workout template table
        self.cursor.execute('''
        CREATE TABLE workout_templates (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            created_date TEXT NOT NULL
        )
        ''')
        
        # Workout exercises (join table between workouts and exercises)
        self.cursor.execute('''
        CREATE TABLE workout_exercises (
            id INTEGER PRIMARY KEY,
            workout_id INTEGER NOT NULL,
            exercise_id INTEGER NOT NULL,
            sets INTEGER NOT NULL,
            reps TEXT NOT NULL,
            rest_time INTEGER,
            FOREIGN KEY (workout_id) REFERENCES workout_templates (id),
            FOREIGN KEY (exercise_id) REFERENCES exercises (id)
        )
        ''')
        
        # Workout sessions (actual performed workouts)
        self.cursor.execute('''
        CREATE TABLE workout_sessions (
            id INTEGER PRIMARY KEY,
            workout_id INTEGER NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT,
            notes TEXT,
            FOREIGN KEY (workout_id) REFERENCES workout_templates (id)
        )
        ''')
        
        # Exercise logs (sets performed during a workout session)
        self.cursor.execute('''
        CREATE TABLE exercise_logs (
            id INTEGER PRIMARY KEY,
            session_id INTEGER NOT NULL,
            exercise_id INTEGER NOT NULL,
            set_number INTEGER NOT NULL,
            weight REAL,
            reps INTEGER,
            completed INTEGER NOT NULL,
            FOREIGN KEY (session_id) REFERENCES workout_sessions (id),
            FOREIGN KEY (exercise_id) REFERENCES exercises (id)
        )
        ''')
        
        # Commit the changes
        self.conn.commit()
        
        # Add some sample data
        self.add_sample_data()
    
    def add_sample_data(self):
        """Add some initial sample data to the database"""
        # Sample exercises
        exercises = [
            ("Bench Press", "Chest", "Barbell", "Lie on a bench and press the weight up"),
            ("Squat", "Legs", "Barbell", "Lower your body by bending your knees"),
            ("Pull-up", "Back", "Body weight", "Pull your body up to a bar"),
            ("Shoulder Press", "Shoulders", "Dumbbells", "Press the weights overhead"),
            ("Deadlift", "Back", "Barbell", "Lift the weight from the ground"),
            ("Bicep Curl", "Arms", "Dumbbells", "Curl the weight towards your shoulder")
        ]
        
        self.cursor.executemany('''
        INSERT INTO exercises (name, muscle_group, equipment, description)
        VALUES (?, ?, ?, ?)
        ''', exercises)
        
        # Sample workout template
        current_date = datetime.now().strftime("%Y-%m-%d")
        self.cursor.execute('''
        INSERT INTO workout_templates (name, description, created_date)
        VALUES (?, ?, ?)
        ''', ("Full Body Workout", "A complete full body workout", current_date))
        
        workout_id = self.cursor.lastrowid
        
        # Sample workout exercises
        workout_exercises = [
            (workout_id, 1, 3, "8-10", 60),  # Bench Press
            (workout_id, 2, 3, "8-10", 90),  # Squat
            (workout_id, 3, 3, "8-10", 60),  # Pull-up
            (workout_id, 5, 3, "8-10", 90)   # Deadlift
        ]
        
        self.cursor.executemany('''
        INSERT INTO workout_exercises (workout_id, exercise_id, sets, reps, rest_time)
        VALUES (?, ?, ?, ?, ?)
        ''', workout_exercises)
        
        self.conn.commit()
    
    def close(self):
        """Close the database connection"""
        if self.conn:
            self.conn.close()
    
    def get_all_exercises(self):
        """Get all exercises from the database"""
        self.cursor.execute("SELECT id, name, muscle_group, equipment FROM exercises")
        return self.cursor.fetchall()
    
    def add_exercise(self, name, muscle_group, equipment, description):
        """Add a new exercise to the database"""
        self.cursor.execute('''
        INSERT INTO exercises (name, muscle_group, equipment, description)
        VALUES (?, ?, ?, ?)
        ''', (name, muscle_group, equipment, description))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_all_workout_templates(self):
        """Get all workout templates"""
        self.cursor.execute("SELECT id, name, description, created_date FROM workout_templates")
        return self.cursor.fetchall()
    
    def get_workout_exercises(self, workout_id):
        """Get all exercises for a specific workout"""
        self.cursor.execute('''
        SELECT e.id, e.name, e.muscle_group, we.sets, we.reps, we.rest_time
        FROM exercises e
        JOIN workout_exercises we ON e.id = we.exercise_id
        WHERE we.workout_id = ?
        ''', (workout_id,))
        return self.cursor.fetchall()
    
    def start_workout_session(self, workout_id):
        """Start a new workout session"""
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('''
        INSERT INTO workout_sessions (workout_id, start_time)
        VALUES (?, ?)
        ''', (workout_id, start_time))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def complete_workout_session(self, session_id, notes=None):
        """Complete a workout session"""
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('''
        UPDATE workout_sessions
        SET end_time = ?, notes = ?
        WHERE id = ?
        ''', (end_time, notes, session_id))
        self.conn.commit()
    
    def log_exercise_set(self, session_id, exercise_id, set_number, weight, reps, completed):
        """Log a completed exercise set"""
        self.cursor.execute('''
        INSERT INTO exercise_logs (session_id, exercise_id, set_number, weight, reps, completed)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (session_id, exercise_id, set_number, weight, reps, completed))
        self.conn.commit()
        return self.cursor.lastrowid
