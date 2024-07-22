from datetime import datetime
from filemanager import FileManager  

class TextFileManager(FileManager):
    """
    Concrete subclass of FileManager for text file operations.
    """

    def open_file(self, file_path: str, mode: str):
        self.file = open(file_path, mode)

    def close_file(self):
        if self.file:
            self.file.close()

    def read_entire_file(self, file_path: str) -> str:
        with open(file_path, 'r') as f:
            return f.read()

    def read_line_from_file(self, file_path: str) -> str:
        with open(file_path, 'r') as f:
            return f.readline()
    
    def read_lines_from_file(self, file_path: str)->list:
        with open(file_path) as f:
            return f.readlines()

    def write_to_file(self, file_path: str, data: str):
        with open(file_path, 'w') as f:
            f.write(data)

    def append_to_file(self, file_path: str, data: str):
        with open(file_path, 'a') as f:
            f.write(data + '\n')  # Ensure new data starts on a new line

    def create_file(self, file_path: str):
        with open(file_path, 'w') as f:
            pass  # Just create an empty file

    def delete_file(self, file_path: str):
        super().delete_file(file_path)  # Use parent method for file deletion

    def get_file_size(self, file_path: str) -> int:
        return super().get_file_size(file_path)  # Use parent method for file size

    def get_file_creation_time(self, file_path: str) -> datetime:
        return super().get_file_creation_time(file_path)  # Use parent method for creation time

    def get_file_modification_time(self, file_path: str) -> datetime:
        return super().get_file_modification_time(file_path)  # Use parent method for modification time

    def find_text_in_file(self, file_path: str, search_text: str):
        """
        Finds the first occurrence of a specific text in a file and returns its location.

        :param file_path: Path to the text file.
        :param search_text: The text to search for.
        :return: A tuple (line_number, character_index) if found, otherwise None.
        """
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                character_index = line.find(search_text)
                if character_index != -1:
                    return (line_number, character_index)
        return None

    def replace_text_in_file(self, file_path: str, old_text: str, new_text: str):
        """
        Replaces all occurrences of old_text with new_text in the specified file.

        :param file_path: Path to the text file.
        :param old_text: The text to be replaced.
        :param new_text: The text to replace with.
        """
        # Read the entire file into memory
        with open(file_path, 'r') as file:
            content = file.read()

        # Replace old_text with new_text
        updated_content = content.replace(old_text, new_text)

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)

# Example usage
if __name__ == "__main__":
    print("This file is not meant to be run directly.")

    text_manager = TextFileManager()

    text_manager.create_file('data.txt')
    
    # Writing data to text file
    data_to_write = "Hello, World!\nThis is a text file."
    text_manager.write_to_file('data.txt', data_to_write)
    
    # Reading entire text file
    print("Reading entire text file:")
    data_read = text_manager.read_entire_file('data.txt')
    print(data_read)
    
    # Appending data to text file
    data_to_append = "Appending new line."
    text_manager.append_to_file('data.txt', data_to_append)
    
    # Reading line from text file
    print("\nReading single line from text file:")
    single_line = text_manager.read_line_from_file('data.txt')
    print(single_line)
    
    # Find text in file
    search_text = "text"
    location = text_manager.find_text_in_file('data.txt', search_text)
    if location:
        print(f"Text '{search_text}' found at line {location[0]}, character {location[1]}")
    else:
        print(f"Text '{search_text}' not found in the file.")

    # Replace text in file
    text_manager.replace_text_in_file('data.txt', 'text', 'document')
    print("Updated File Content:")
    updated_content = text_manager.read_entire_file('data.txt')
    print(updated_content)

    text_manager.delete_file('data.txt')
    print("Finished Successfully")
