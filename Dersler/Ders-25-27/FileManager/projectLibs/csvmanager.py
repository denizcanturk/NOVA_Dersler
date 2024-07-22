import csv
import json
from datetime import datetime
from .filemanager import FileManager

class CSVManager(FileManager):
    """
    Concrete subclass of FileManager for CSV file operations.
    """

    def open_file(self, file_path: str, mode: str):
        self.file = open(file_path, mode, newline='')

    def close_file(self):
        if self.file:
            self.file.close()

    def read_entire_file(self, file_path: str) -> list:
        data = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return data

    def read_line_from_file(self, file_path: str) -> list:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            return next(reader)

    def write_to_file(self, file_path: str, data: list):
        """
            Creates and writes data [list] to file
        """
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

    def append_to_file(self, file_path: str, data: list):
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

    def csv_to_json(self, csv_file_path: str, json_file_path: str):
        """
        Converts a CSV file to a JSON file format and writes it to the given JSON file path.
        
        :param csv_file_path: Path to the input CSV file.
        :param json_file_path: Path to the output JSON file.
        """
        data = {}
        
        # Read CSV file
        with open(csv_file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            
            # Extract headers
            headers = next(reader)
            
            # Initialize lists for each header
            for header in headers:
                data[header] = []
            
            # Read rows and append data to corresponding header lists
            for row in reader:
                for header, value in zip(headers, row):
                    data[header].append(value)
        
        # Write JSON file
        with open(json_file_path, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
            
    def create_file(self, file_path: str):
        # Create an empty CSV file with headers
        with open(file_path, 'w', newline='') as csvfile:
            pass  # Just create an empty file

    def delete_file(self, file_path: str):
        super().delete_file(file_path)  # Use parent method for file deletio    "n

    def get_file_size(self, file_path: str) -> int:
        return super().get_file_size(file_path)  # Use parent method for file size

    def get_file_creation_time(self, file_path: str) -> datetime:
        return super().get_file_creation_time(file_path)  # Use parent method for creation time

    def get_file_modification_time(self, file_path: str) -> datetime:
        return super().get_file_modification_time(file_path)  # Use parent method for modification time

    def replace_value_in_file(self, file_path: str, old_value: str, new_value: str):
        """
        Searches for all occurrences of old_value in the CSV and replaces them with new_value.

        :param file_path: Path to the CSV file.
        :param old_value: The value to search for.
        :param new_value: The value to replace it with.
        """
        # Read the entire file into memory
        data = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for cell in row:
                    if cell == old_value:
                        data.append(new_value)
                    else:
                        data.append(cell)

                # Replace old_value with new_value in each row
                # data.append([new_value if cell == old_value else cell for cell in row])

        # Write the modified data back to the file
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

    def update_phone_number_by_name(self, 
                                    file_path: str,
                                    colToSearch : str,
                                    valToChange : str,
                                    user_name: str, 
                                    newValToRecord: str):
        """
        Updates the phone number for a given user name in the CSV file.

        :param file_path: Path to the CSV file.
        :param user_name: The name of the user whose phone number is to be updated.
        :param newValToRecord: The new phone number to assign to the user.
        """
        # Read the entire file into memory
        data = []
        reference_index = None
        target_index = None
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            # Find the index for reference and target columns
            try:
                reference_index = headers.index(colToSearch)
                target_index = headers.index(valToChange)
            except ValueError:
                raise ValueError(f"CSV does not contain {colToSearch} or {valToChange} headers")
            data.append(headers)  # Append headers back to data

            for row in reader:
                if row[reference_index] == user_name:
                    row[target_index] = newValToRecord  # Update the phone number
                data.append(row)

        # Write the modified data back to the file
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

# Example usage
if __name__ == "__main__":
    print("This file is not meant to be run directly.")
    exit()

    csv_manager = CSVManager()

    csv_manager.create_file('data.csv')
    
    # Writing data to CSV
    data_to_write = [
        ['Name', 'Age', 'City', 'Phone Number'],
        ['John Doe', '30', 'New York', '123-456-7890'],
        ['Jane Smith', '25', 'Los Angeles', '987-654-3210'],
        ['Deniz', '28', 'Chicago', '555-678-1234']
    ]
    csv_manager.write_to_file('data.csv', data_to_write)
    
    # Reading entire CSV
    print("Original Data:")
    data_read = csv_manager.read_entire_file('data.csv')
    for row in data_read:
        print(row)
    
    # Appending data to CSV
    data_to_append = [
        ['Tom Brown', '40', 'Chicago']
    ]
    csv_manager.append_to_file('data.csv', data_to_append)
    
    # Reading line from CSV
    print("\nReading single line from CSV:")
    single_line = csv_manager.read_line_from_file('data.csv')
    print(single_line)
    
    # Update phone number for 'Deniz'
    csv_manager.update_phone_number_by_name('data.csv',"Name","Phone Number", 'Deniz', '555-123-4567')
    print("Updated Data:")
    print(csv_manager.read_entire_file('data.csv'))
    
    csv_manager.delete_file('data.csv')
