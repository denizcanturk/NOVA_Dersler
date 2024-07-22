from projectLibs.txtmanager import TextFileManager
from projectLibs.csvmanager import CSVManager
from projectLibs.jsonmanager import JSONManager

def main():
    # Text file operations
    text_manager = TextFileManager()

    print("--- Text File Operations ---")
    text_manager.create_file('Outputs/data.txt')
    text_manager.write_to_file('Outputs/data.txt', "Hello, World!\nThis is a text file.")
    data_read = text_manager.read_entire_file('Outputs/data.txt')
    print("Reading entire text file:")
    print(data_read)
    text_manager.append_to_file('Outputs/data.txt', "\nAppending new line.")
    single_line = text_manager.read_line_from_file('Outputs/data.txt')
    print("\nReading single line from text file:")
    print(single_line)
    #text_manager.delete_file('Outputs/data.txt')

    # CSV file operations
    csv_manager = CSVManager()

    print("\n--- CSV File Operations ---")
    csv_manager.create_file('Outputs/data.csv')
    data_to_write_csv = [
        ['Name', 'Age', 'City'],
        ['John Doe', '30', 'New York'],
        ['Jane Smith', '25', 'Los Angeles']
    ]
    csv_manager.write_to_file('Outputs/data.csv', data_to_write_csv)
    data_read_csv = csv_manager.read_entire_file('Outputs/data.csv')
    print("Reading entire CSV:")
    for row in data_read_csv:
        print(row)
    data_to_append_csv = ['Tom Brown', '40', 'Chicago']
    csv_manager.append_to_file('Outputs/data.csv', data_to_append_csv)
    single_line_csv = csv_manager.read_line_from_file('Outputs/data.csv')
    print("\nReading single line from CSV:")
    print(single_line_csv)
    #csv_manager.delete_file('Outputs/data.csv')

    # JSON file operations
    json_manager = JSONManager()

    print("\n--- JSON File Operations ---")
    json_manager.create_file('Outputs/data.json')
    data_to_write_json = {
        "users": [
            {"name": "John Doe", "age": 30, "city": "New York"},
            {"name": "Jane Smith", "age": 25, "city": "Los Angeles"}
        ]
    }
    json_manager.write_to_file('Outputs/data.json', data_to_write_json)
    data_read_json = json_manager.read_entire_file('Outputs/data.json')
    print("Reading entire JSON:")
    print(data_read_json)
    data_to_append_json = {"name": "Tom Brown", "age": 40, "city": "Chicago"}
    json_manager.append_to_file('Outputs/data.json', data_to_append_json)
    #json_manager.read_line_from_file('Outputs/data.json')  # Not really applicable for JSON, but mimicking for consistency
    #print("\nReading single line from JSON:")
    #print(single_line_json)
    #json_manager.delete_file('Outputsdata.json')


if __name__ == "__main__":
    main()
