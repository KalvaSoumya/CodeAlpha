import os
import shutil

def organize_files(directory):
    # Define the file types and their corresponding folders
    file_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'audio': ['.mp3', '.wav', '.aac'],
        'videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'archives': ['.zip', '.rar', '.tar', '.gz']
    }

    # Create folders for each file type if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file type and move the file to the corresponding folder
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                new_filename = generate_new_filename(folder, file_ext)
                new_file_path = os.path.join(directory, folder, new_filename)
                shutil.move(file_path, new_file_path)
                print(f"Moved {filename} to {new_file_path}")
                moved = True
                break

        # If file type is not recognized, move it to 'others' folder
        if not moved:
            others_folder = os.path.join(directory, 'others')
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            new_file_path = os.path.join(others_folder, filename)
            shutil.move(file_path, new_file_path)
            print(f"Moved {filename} to {new_file_path}")

def generate_new_filename(folder, ext):
    # Example of generating a new filename based on the current timestamp and folder type
    import time
    timestamp = time.strftime("%Y%m%d%H%M%S")
    new_filename = f"{folder}_{timestamp}{ext}"
    return new_filename

# Usage
directory_to_organize = '/path/to/your/directory'
organize_files(directory_to_organize)