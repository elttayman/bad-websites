import os
import json

def remove_duplicates(links):
    # Convert the list to a set to remove duplicates, then convert back to a list
    unique_links = list(set(links))
    return unique_links

def remove_duplicates_and_save(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
        original_links = data['links']
        # Remove duplicates from the list of links
        unique_links = remove_duplicates(data['links'])
        
        # Check if duplicates were removed
        if len(original_links) != len(unique_links):
            with open(output_file, 'w') as outfile:
                data['links'] = unique_links
                json.dump(data, outfile, indent=4)
                print(f"Duplicates removed from {input_file} and saved as {output_file}")
        else:
            print(f"No duplicates found in {input_file}, skipping...")

def merge_json_files(directory):
    merged_data = {"links": []}

    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            output_file = os.path.join(directory, filename)
            print(output_file)
            remove_duplicates_and_save(file_path, output_file)
            
            # Read the modified file with duplicates removed
            with open(output_file, 'r') as file:
                data = json.load(file)
                merged_data['links'].extend(data['links'])

    # Remove duplicates from the merged data
    merged_data['links'] = remove_duplicates(merged_data['links'])
    
    # Sort the links alphabetically
    merged_data['links'] = sorted(merged_data['links'])

    return merged_data

def save_merged_data(merged_data, output_file):
    with open(output_file, 'w') as outfile:
        json.dump(merged_data, outfile, indent=4)

if __name__ == "__main__":
    directory = "separated"
    output_file = "websites.json"

    merged_data = merge_json_files(directory)
    save_merged_data(merged_data, output_file)
    print("Merged JSON files and saved as", output_file)
