import json
import shutil
import os

def process_images(json_file, target_folder):
    try:
        # Construct the full path for the target folder
        full_target_folder = os.path.join('test_finetune', target_folder)

        # Create target folder if it doesn't exist
        if not os.path.exists(full_target_folder):
            os.makedirs(full_target_folder)

        # Construct the full path for the JSON file
        full_json_file = os.path.join('test_finetune', json_file)

        # Read the JSON file
        with open(full_json_file, 'r') as file:
            data = json.load(file)

        # Process each image
        for image in data['images']:
            # Construct the full original file path
            original_path = os.path.join('test_finetune', image['file_name'])

            # Define the new path
            new_path = os.path.join(full_target_folder, os.path.basename(original_path))

            # Move the file
            shutil.move(original_path, new_path)

            # Update the file path in JSON data
            image['file_name'] = os.path.join(target_folder, os.path.basename(original_path))

        # Write the updated JSON back to the file
        with open(full_json_file, 'w') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
process_images('train_dat.json', 'train_images')
process_images('test_dat.json', 'test_images')

