import os
from pydub import AudioSegment
import subprocess
import shutil

def split_and_reconnect(input_string, splitter):
    # Split the string by "."
    parts = input_string.split(splitter)
    
    # Remove the last item from the list
    parts.pop()
    
    # Reconnect the remaining parts with "."
    result = splitter.join(parts)
    
    return result

def checkFolderExistorCreate(path):
    if not os.path.exists(path):
        # Create the folder and any necessary parent folders
        os.makedirs(path)
        print(f"Folder '{path}' created.")

def checkFileExist(path):
    return os.path.exists(path) 

global_folder_path = 'C:/test/doyof'
folder_path_output = 'C:/testMP3/doyof'

# Function to check files in the folder
def check_files_in_folder(folder_path):
    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file extension
            _, extension = os.path.splitext(file_name)
            
            # Check if the file extension is 'mp3'
            if extension.lower() != '.mp3' and extension.lower() != '.txt':
                folder = split_and_reconnect(file_path[len(global_folder_path):], '\\')
                output_file_path = split_and_reconnect(folder_path_output + folder + '/' + file_name, '.') + '.mp3'
                output_file_path = output_file_path.replace("\\", "/")
                print(f"{file_path}  ==>  {output_file_path}")
                if not checkFileExist(output_file_path):
                    trimmedFile = split_and_reconnect(file_path[len(global_folder_path):], '.')
                    checkFolderExistorCreate(folder_path_output + folder)
                    
                    command = ['ffmpeg', '-i', file_path.replace('\\', '/'), output_file_path]
                    result = subprocess.run(command, capture_output=True, text=True, check=True)
                else:
                    print(f"file already exists: {output_file_path}")
            elif extension.lower() == '.mp3':
                folder = split_and_reconnect(file_path[len(global_folder_path):], '\\')
                output_file_path = split_and_reconnect(folder_path_output + folder + '/' + file_name, '.') + '.mp3'
                output_file_path = output_file_path.replace("\\", "/")
                print(f"{file_path}  ==>  {output_file_path}")
                if not checkFileExist(output_file_path):
                    trimmedFile = split_and_reconnect(file_path[len(global_folder_path):], '.')
                    checkFolderExistorCreate(folder_path_output + folder)
                    
                    shutil.copy(file_path.replace('\\', '/'), (folder_path_output + folder + '/').replace('\\', '/'))
        else :
            check_files_in_folder(file_path)

# Call the function
check_files_in_folder(global_folder_path)