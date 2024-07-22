# Import required modules
import subprocess

# Define the filenames of the examples
filenames = ["Calculat.py", "DrawingApp.py", "rock_paper.py", "turt.py", "turt2.py"]

# Run each example
for filename in filenames:
    print(f"Running {filename}...")
    try:
        subprocess.run(["python", filename], check=True)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except subprocess.CalledProcessError:
        print(f"Error running {filename}.")
    print("\n")
