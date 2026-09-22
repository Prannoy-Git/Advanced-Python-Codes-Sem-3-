import csv
import json

def read_csv(file_name):
    with open(file_name, "r", newline="") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

def write_json(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

def convert_csv_to_json(input_file, output_file):
    data = read_csv(input_file)
    write_json(output_file, data)
    return data

if __name__ == "__main__":

    input_file = "students.csv"
    output_file = "students.json"

    sample_data = """Roll No, Name, Branch, Marks
1,Prannoy M,CSE,85
2,Rahul S,Mechanical,78
3,Aditya A,Electronics,91
4,Akash M,CSE,88
"""

    with open(input_file, "w", newline="") as f:
        f.write(sample_data)

    print("CSV file created")
    
    with open(input_file, "r") as f:
        print(f.read())

    data = convert_csv_to_json(input_file, output_file)

    print("Number of rows converted:", len(data))
    print("JSON file created")

    with open(output_file, "r") as f:
        print(f.read())