import os

def process_files(folder_path):
    # Get a list of all files in the folder
    all_files = os.listdir(folder_path)

    # Iterate through each file in the folder
    for file_name in all_files:
        # Check if the file is a text file
        if file_name.lower().endswith('.txt'):
            # Extract the base name without extension
            base_name = os.path.splitext(file_name)[0]
            # print(f'{base_name }"\n"')
            # Construct the corresponding image file name
            image_file_name = f"{base_name}.jpg"
            print(f'{image_file_name }"\n"')
            # Check if the image file exists
            if not os.path.exists(os.path.join(folder_path, image_file_name)):
                # If there is no matching image file, delete the text file
                text_file_path = os.path.join(folder_path, file_name)
                os.remove(text_file_path)
                print(f"Deleted {file_name}")

# Specify the folder path
folder_path = "D:/VisualStudioPython/Virtual Environment/Projects/Anti Spoofing(Liveliness) Detector/Datasets/Fake2"

# Call the function to process the files
process_files(folder_path)
