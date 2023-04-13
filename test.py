import os

os.mkdir("./test")
# Define the file path and contents
file_path = './test/new_file.txt'
file_contents = 'This is the contents of the new file.'

# Create the file
with open(file_path, 'w') as f:
    f.write(file_contents)

# Commit the file to the repository
os.system('git add {} && git commit -m "Added new file" && git push'.format(file_path))
