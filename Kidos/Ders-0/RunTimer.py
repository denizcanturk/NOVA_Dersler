import multiprocessing
import subprocess
import time

# Define the filenames of the examples
filenames = ["Calculat.py", "DrawingApp.py", "rock_paper.py", "turt.py", "rollingTxt.py"]

# Function to run a single example for a specific duration
def run_example_for_duration(filename, duration):
    try:
        print(f"Running {filename}...")
        start_time = time.time()
        process = subprocess.Popen(["python", filename])
        while time.time() - start_time < duration:
            if process.poll() is not None:  # Check if the process has terminated
                break
            time.sleep(1)  # Wait for 1 second
        if process.poll() is None:  # If the process is still running after the duration
            print(f"Terminating {filename}...")
            process.terminate()  # Terminate the process
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

# Create a multiprocessing pool
pool = multiprocessing.Pool()

# Keep the last example running indefinitely
run_example_for_duration(filenames, float('inf'))

# Run each example for approximately 30 seconds
#for filename in filenames[:-1]:
#    run_example_for_duration(filename, 30)



# Close the pool
pool.close()
pool.join()
