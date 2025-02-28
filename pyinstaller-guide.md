# Compiling Your Workout Tracker Application in VSCode

This guide will walk you through the process of converting your Python application into a standalone executable using PyInstaller.

## Prerequisites

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Make sure your application runs correctly before packaging

## Setting Up the Project Structure

Ensure your project has a structure like this:

```
workout_tracker/
├── main.py
├── database/
│   └── db_manager.py
├── frames/
│   ├── home_frame.py
│   ├── exercise_frame.py
│   ├── workout_frame.py
│   ├── history_frame.py
│   └── stats_frame.py
└── dialogs/
    └── exercise_dialog.py
```

## Creating a Spec File (Optional but Recommended)

1. Generate a basic spec file:
   ```
   pyinstaller --name WorkoutTracker main.py
   ```

2. Modify the generated `WorkoutTracker.spec` file to include additional resources if needed.

## Building the Executable in VSCode

### Method 1: Using the Terminal in VSCode

1. Open VSCode terminal (Terminal > New Terminal)

2. Navigate to your project directory

3. Run PyInstaller with the spec file:
   ```
   pyinstaller WorkoutTracker.spec
   ```

   Or directly with the main script:
   ```
   pyinstaller --onefile --windowed --name WorkoutTracker main.py
   ```

### Method 2: Create a VSCode Task

1. Press `Ctrl+Shift+P` and search for "Configure Tasks"

2. Select "Create tasks.json file from template"

3. Choose "Others"

4. Replace the content with:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Build Executable",
            "type": "shell",
            "command": "pyinstaller --onefile --windowed --name WorkoutTracker main.py",
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "reveal": "always",
                "panel": "new"
            }
        }
    ]
}
```

5. Now you can build your application by pressing `Ctrl+Shift+B`

## PyInstaller Options Explained

- `--onefile`: Creates a single executable file containing everything
- `--windowed`: Prevents a console window from opening when the app runs
- `--name WorkoutTracker`: Sets the name of the output executable
- `--icon=path/to/icon.ico`: Adds a custom icon to the executable (optional)

## Troubleshooting Common Issues

1. **Missing modules**: If PyInstaller misses some imports, explicitly include them:
   ```
   pyinstaller --onefile --windowed --name WorkoutTracker --hidden-import=tkinter main.py
   ```

2. **Missing data files**: Use the `--add-data` option:
   ```
   pyinstaller --onefile --windowed --name WorkoutTracker --add-data="resources;resources" main.py
   ```

3. **SQLite issues**: Sometimes SQLite needs special handling:
   ```
   pyinstaller --onefile --windowed --name WorkoutTracker --hidden-import=sqlite3 main.py
   ```

## Running the Compiled Application

After successful compilation, you'll find your executable in the `dist` folder. You can distribute this single file to run your application on any compatible system without requiring Python or the dependencies to be installed.
