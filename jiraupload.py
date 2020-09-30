import requests
import os
from zipfile import ZipFile
# Setup authentication credentials
credentials  = requests.auth.HTTPBasicAuth('dnethaji','sGSH9?iu')
# JIRA required header (as per documentation)
headers = { 'X-Atlassian-Token': 'no-check' }
# Setup multipart-encoded file
#files = [ ('file', ('sampleDir.zip', open('sampleDir.zip','rb'), 'application/zip')) ]
#print(files)
files = []
filelist = []
with ZipFile('htmlreports.zip', 'w') as zipObj:
    for root, dirnames, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if filename.endswith('.html'):
                fname = os.path.join(root, filename)
                print('Filename: {}'.format(fname))
                filelist.append(fname)
                zipObj.write(fname)
                #files.append(open(fname, 'rb'))
        break
zipObj.close()
files = [ ('file', ('htmlreports.zip', open('htmlreports.zip','rb'), 'application/zip')) ]
1:35
r = requests.post("https://jira.jnj.com/rest/api/latest/issue/AFHS-2453/attachments", auth=credentials, files=files, headers=headers)
print(files)
#r = requests.post("https://medband.atlassian.net/rest/api/latest/issue/GA-5/attachments", auth=credentials, files=files, headers=headers)
print(r.status_code)
print(r.reason)
