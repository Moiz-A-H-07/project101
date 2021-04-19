import os
import dropbox
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:    
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)  
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
def main():
    access_token = 'sl.AvNC_Lx70es7ElD0M3LI03oGMsh9miWmUhwiPNzrQKmFzKFKpQxAWXB1gDzun6XF6H9Jw5DmqdAJu1GYJKRVUqpOVKd_oTSOQc78X8Xe_a1On0fMo2tY5eMmRp7_aKlzAfgDCG8'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : -"))
    file_to = input("enter the full path to upload to dropbox:- ")  

    # API v2
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()