import os
import re

rootfolder_path = "/Users/mkucher/Documents/Gathers-bot/data"

# Walk the directory tree bottom-up
for dirpath, dirnames, filenames in os.walk(rootfolder_path, topdown=False):
    # Process directories
    for dirname in dirnames:
        new_dirname = ' '.join(word for word in dirname.split() if len(word) <= 18)
        if new_dirname != dirname:
            os.rename(os.path.join(dirpath, dirname), os.path.join(dirpath, new_dirname))
    # Process files
    for filename in filenames:
        if filename.endswith('.md'):
            name, ext = os.path.splitext(filename)
            new_name = ' '.join(word for word in name.split() if len(word) <= 18)
            new_filename = new_name + ext
            if new_filename != filename:
                os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, new_filename))