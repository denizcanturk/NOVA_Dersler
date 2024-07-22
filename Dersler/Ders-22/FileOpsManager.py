import os

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        """Reads the entire content of the file."""
        try:
            with open(self.file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return f"An error occurred: {e}"

    def write_file(self, content):
        """Writes content to the file, overwriting if it already exists."""
        try:
            with open(self.file_path, 'w') as file:
                file.write(content)
                return "Write operation successful."
        except Exception as e:
            return f"An error occurred: {e}"

    def append_to_file(self, content):
        """Appends content to the file."""
        try:
            with open(self.file_path, 'a') as file:
                file.write(content)
                return "Append operation successful."
        except Exception as e:
            return f"An error occurred: {e}"

    def file_exists(self):
        """Checks if the file exists."""
        return os.path.exists(self.file_path)

    def delete_file(self):
        """Deletes the file."""
        try:
            if os.path.exists(self.file_path):
                os.remove(self.file_path)
                return "File deleted successfully."
            else:
                return "File does not exist."
        except Exception as e:
            return f"An error occurred: {e}"

# Example usage
file_manager = FileManager("example.txt")

# Write to file
print(file_manager.write_file("Hello, world!"))

# Read from file
print(file_manager.read_file())

# Append to file
print(file_manager.append_to_file("\nThis is an appended line."))

# Read from file again
print(file_manager.read_file())

# Check if file exists
print(file_manager.file_exists())

# Delete the file
print(file_manager.delete_file())

# Check if file exists again
print(file_manager.file_exists())
