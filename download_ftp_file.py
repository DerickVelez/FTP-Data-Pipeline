import ftplib
import zipfile

HOSTNAME = "localhost"
USERNAME = "derick1"
PASSWORD = "Workeye29"

ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
 
# force UTF-8 encoding
ftp_server.encoding = "utf-8"

filename = "CRED_DATA.zip"
 
# Write file in binary mode
with open(filename, "wb") as file:
    ftp_server.retrbinary(f"RETR {filename}", file.write)
 
# Close the Connection
ftp_server.quit()

with zipfile.ZipFile(f"{filename}","r") as zip_ref:
    zip_ref.extractall("D:\development\python\DATAPIPELINEPROJECT\extracted")


# # Enter File Name with Extension
# filename = "gfg.txt"
 
# # Read file in binary mode
# with open(filename, "rb") as file:
#     # Command for Uploading the file "STOR filename"
#     ftp_server.storbinary(f"STOR {filename}", file)