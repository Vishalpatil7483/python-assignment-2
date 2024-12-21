# Example 7: Archiving a Directory 
print("Name: Rakshitha P \nReg no: 23BTIT145")
import shutil
import os

# Create a directory to archive
os.makedirs('archive_me', exist_ok=True)

with open(os.path.join('archive_me', 'file1.txt'), 'w') as f:
    f.write('This file is in the archive directory.')

with open(os.path.join('archive_me', 'file2.txt'), 'w') as f:
    f.write('Another file in the archive directory.')

# Create a zip archive
shutil.make_archive('archive', 'zip', 'archive_me')

print('Directory "archive_me" archived as "archive.zip".')