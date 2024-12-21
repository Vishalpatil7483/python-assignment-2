# Example 8: Extracting an Archive 
print("Name: Rakshitha P \nReg no: 23BTIT145")
import shutil

# Extract the archive created in Example 7
shutil.unpack_archive('archive.zip', 'extracted_files')

print('Archive "archive.zip" extracted to "extracted_files" directory.')