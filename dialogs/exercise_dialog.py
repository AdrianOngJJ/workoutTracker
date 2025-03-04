# dialogs/exercise_dialog.py
import tkinter as tk
from tkinter import ttk

class ExerciseDialog(tk.Toplevel):
    def __init__(self, parent, exercise=None, callback=None):
        """
        Dialog for adding or editing an exercise
        
        Args:
            parent: The parent window
            exercise: Optional tuple of (id, name, muscle_group, equipment, description)
                     If provided, dialog opens in edit mode
            callback: Function to call with the result when dialog is closed
        """
        super().__init__(parent)
        self.parent = parent
        self.exercise = exercise
        self.callback = callback
        
        # Configure dialog
        self.title("Add Exercise" if not exercise else "Edit Exercise")
        self.geometry("400x350")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        
        # Create widgets
        self.create_widgets()
        
        # Fill fields if editing
        if exercise:
            self.name_entry.insert(0, exercise[1])
            self.muscle_var.set(exercise[2])
            self.equipment_entry.insert(0, exercise[3])
            if len(exercise) > 4:
                self.description_text.insert("1.0", exercise[4])
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill="both", expand=True)
        
        # Name field
        ttk.Label(main_frame, text="Exercise Name:").grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = ttk.Entry(main_frame, width=30)
        self.name_entry.grid(row=0, column=1, sticky="ew", pady=5)
        
        # Muscle group field
        ttk.Label(main_frame, text="Muscle Group:").grid(row=1, column=0, sticky="w", pady=5)
        muscle_groups = ["Chest", "Back", "Legs", "Shoulders", "Arms", "Core", "Full Body"]
        self.muscle_var = tk.StringVar()
        muscle_combo = ttk.Combobox(main_frame, textvariable=self.muscle_var, values=muscle_groups)
        muscle_combo.grid(row=1, column=1, sticky="ew", pady=5)
        
        # Equipment field
        ttk.Label(main_frame, text="Equipment:").grid(row=2, column=0, sticky="w", pady=5)
        self.equipment_entry = ttk.Entry(main_frame, width=30)
        self.equipment_entry.grid(row=2, column=1, sticky="ew", pady=5)
        
        # Description field
        ttk.Label(main_frame, text="Description:").grid(row=3, column=0, sticky="nw", pady=5)
        self.description_text = tk.Text(main_frame, width=30, height=6)
        self.description_text.grid(row=3, column=1, sticky="ew", pady=5)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=15)
        
        ttk.Button(button_frame, text="Cancel", command=self.cancel).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Save", command=self.save).pack(side="left", padx=5)
    
    def save(self):
        # Collect data
        name = self.name_entry.get().strip()
        muscle_group = self.muscle_var.get()
        equipment = self.equipment_entry.get().strip()
        description = self.description_text.get("1.0", "end-1c").strip()
        
        # Validate
        if not name or not muscle_group:
            tk.messagebox.showerror("Error", "Name and muscle group are required")
            return
        
        # Return data through callback
        if self.callback:
            if self.exercise:  # Edit mode
                exercise_id = self.exercise[0]
                self.callback((exercise_id, name, muscle_group, equipment, description))
            else:  # Add mode
                self.callback((None, name, muscle_group, equipment, description))
        
        self.destroy()
    
    def cancel(self):
        self.destroy()

# Add similar dialog classes for:
# - StartWorkoutDialog: For selecting and starting a workout
# - WorkoutDialog: For creating/editing workout templates
# - LogSetDialog: For logging a set during a workout
