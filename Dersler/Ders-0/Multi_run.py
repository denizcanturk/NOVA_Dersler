import multiprocessing
import subprocess

# Define the filenames of the examples
filenames = [ "turt.py", "Calculat.py", "DrawingApp.py", "rock_paper.py", "rollingTxt.py", "saat.py"]

# Function to run a single example
def run_example(filename):
    try:
        print(f"Running {filename}...")
        subprocess.run(["python", filename], check=True)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except subprocess.CalledProcessError:
        print(f"Error running {filename}.")

# Create a multiprocessing pool
pool = multiprocessing.Pool(processes=len(filenames))

# Run each example concurrently
pool.map(run_example, filenames)

# Close the pool
pool.close()
pool.join()
