import urllib2
import requests
import os
import json
import settings as default_settings

os.system('mkdir Files')

def download_file(url, name):
    local_filename = name
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open('Files/' + local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

default_settings_dict = {}
for key in dir(default_settings):
    default_settings_dict[key] = getattr(default_settings, key)

x = urllib2.urlopen(default_settings_dict['URL']).read()
responses = json.loads(x)['responses']

for response in responses:
        if default_settings_dict['DOCUMENT_FIELD'] in response["answers"]:
            download_file(str(response['answers'][default_settings_dict['DOCUMENT_FIELD']]), str(response['answers'][default_settings_dict['LAST_NAME_FIELD']]) + "_" + str(response['answers'][default_settings_dict['FIRST_NAME_FIELD']]))
