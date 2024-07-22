from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Initialize the GoogleAuth instance
gauth = GoogleAuth()

gauth.LoadCredentialsFile("/home/debinci/Desktop/NOVA_Dersler/Demos/credentials.json")

# Authenticate if necessary (this will open a browser window for authentication)
if not gauth.credentials:
    gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

# Save the current credentials to a file
gauth.SaveCredentialsFile("/home/debinci/Desktop/NOVA_Dersler/Demos/credentials.json")

# Create a GoogleDrive instance with authenticated GoogleAuth instance
drive = GoogleDrive(gauth)

# List the files in your Google Drive
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in file_list:
    print(f"title: {file['title']}, id: {file['id']}")