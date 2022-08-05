import dropbox
def upload_file():
    dropbox_access_token = 'sl.BMtJ_zGYMCbZUn4w7Z4MgloVr9R-1uKk__UYz7QshlEMG1PNgnCv4i9E_bSHOx7AxZnaIheImfPi4CaPXPnv5Co9ZyQai2oFqlr1WBGqidToOODr83DLcq-WfW03gqK2p08_CXsSIBbt'
    dropbox_path= "/Python Network Scanner/scanner.log"
    computer_path="/home/pi/Network Scanner/scanner.log"
    client = dropbox.Dropbox(dropbox_access_token)
    print("[SUCCESS] dropbox account linked")
    client.files_upload(open(computer_path, "rb").read(), dropbox_path)
    print("[UPLOADED] {}".format(computer_path))
    
