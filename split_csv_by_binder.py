import csv
import os
import argparse

def split_csv_by_binder(input_file):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    binder_data = {}

    # Read the input CSV and organize rows by Binder Name
    with open(input_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            binder_name = row['Binder Name']
            if binder_name not in binder_data:
                binder_data[binder_name] = []
            binder_data[binder_name].append(row)

    # Create separate CSV files for each Binder Name in the output directory
    for binder_name, rows in binder_data.items():
        # Clean the binder name for use as a filename
        filename = f"{binder_name.replace(' ', '').replace('/', '_')}.csv"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    print(f"CSV files have been created in the '{output_dir}' directory based on Binder Name.")


# Set up command-line argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a CSV file into separate files based on Binder Name")
    parser.add_argument("input_file", help="Path to the input CSV file")
    args = parser.parse_args()

    # Run the function with the provided input file
    split_csv_by_binder(args.input_file)
