import dropbox
def upload_file():
    dropbox_access_token = 'Your access token'
    dropbox_path= "Your path, Example. (/Python Network Scanner/scanner.log)"
    computer_path="Your local path, Example. (/home/pi/Network Scanner/scanner.log)"
    client = dropbox.Dropbox(dropbox_access_token)
    print("[SUCCESS] dropbox account linked")
    client.files_upload(open(computer_path, "rb").read(), dropbox_path)
    print("[UPLOADED] {}".format(computer_path))
    
