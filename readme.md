# Original Task

Write a file hosting with following requirements:

- You can log in or register
- Your files are listed in the profile
- You can add, download or delete any of your files
- You can not have more than 100 files
- Directories are not supported
- Direct file links does not require authorization
- If any of the users already have an uploaded file, a duplicate of this file is not created in the file system, but in the profile this file appears under the same name with which it was loaded

# Installation

    pip install -Ur requirements.txt
    psql -c "CREATE DATABASE asd WITH ENCODING 'UTF8'"
    touch asd/settings/local.py

Then add your google api keys to local settings
