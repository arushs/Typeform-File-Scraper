import csv
import requests
import os
from urlparse import urlparse
import settings as default_settings

os.system('mkdir Files')
downloaded_files = 0
failed_output = open("failed.txt", "w")
default_settings_dict = {}
for key in dir(default_settings):
    default_settings_dict[key] = getattr(default_settings, key)

def download_file(url, name):
    local_filename = name
    # NOTE the stream=True parameter
    if (url.find("typeform") == -1):
        try:
            o = urlparse(url)
            if (url.find("drive.google") != -1):
                key = o.path[o.path.find("/d/"):]
                key = key[:-5]
                key = key[3:]
                newLink = "https://docs.google.com/uc?authuser=0&id=" + key + "&export=download"
                r = requests.get(newLink, stream=True)
                with open('Files/' + local_filename + ".pdf", 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk: # filter out keep-alive new chunks
                            f.write(chunk)
                            f.flush()
                return local_filename
            elif (url.find("dropbox") != -1):
                newUrl = url[:-1] + "1"
                r = requests.get(newUrl, stream=True)
                with open('Files/' + local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk: # filter out keep-alive new chunks
                            f.write(chunk)
                            f.flush()
            return local_filename
        except:
            failed_output.write(name+"\n")
    else:
        parsed_link = url[url.find("results"):]
        parsed_link = parsed_link[8:-9]
        new_url = 'https://api.typeform.com/v0/form/'+ default_settings_dict['FORM_KEY'] + '/fields/' + default_settings_dict['ADVANCED_DOCUMENT_FIELD'] + '/blob/' + parsed_link + '?key=' + default_settings_dict['API_KEY']
        r = requests.get(new_url, stream=True)
        with open('Files/' + local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()

with open(default_settings_dict['CSV_FILE'], 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print row['Name']
        link = row["Url"]
        o = urlparse(link)
        path = o.path
        if (path != "None"):
            end = path[path.find("."):]
            if (end.find('download') != -1):
                end = end[:end.find('download') - 1]
                print end
            if (end == ".jpg"):
                f.write(o.geturl())
            else :
                name = row["Name"]
                name_list = name.split();
                reversed_name_list = reversed(name_list)
                new_name = "_".join(reversed_name_list)
                if (path.find('.') != -1):
                    download_file(link, new_name + end)
                else:
                    download_file(link, new_name)
