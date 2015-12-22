# Typeform File Scraper

## Introduction

There are two scripts in this repo.
- basic_downloader.py

  Will download files from a given Typeform api link. Just fill in the settings.py file as appropriate. Their API is broken so this will never download all the files, especially if people give you dropbox or google drive links.

- advanced_downloader.py

  Will download files from a given CSV files that has two columns. One for names, and one for the links. This will download files not only from Typeform but from dropbox and google drive. The use of this is for the situation when people submit their own links to your Typeform. I recommend downloading all the responses as a CSV, and then splicing the csv so it only has names and urls.

  The settings file is a bit more advanced in this. You need to fill out the file with the DOCUMENT_FIELD as well as your API_KEY and FORM_KEY. The DOCUMENT_FIELD is the number of the field you want to download. It can be found if you look at your CSV file when you download it.

## Contributions

Send Pull Requests!
