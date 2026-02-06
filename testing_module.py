import os

# Get current working directory
current_dir = os.getcwd()

print(type(current_dir))
print("Current directory:", current_dir)

# List all files and folders in the current directory
items = os.listdir(current_dir)
print("Contents:")
for item in items:
    print(item)


import os

# Create a new directory
os.mkdir("test_folder")

print(os.path)
# Check if a directory exists
if os.path.exists("test_folder"):
    print("Folder created!")

# Remove the directory
os.rmdir("test_folder")