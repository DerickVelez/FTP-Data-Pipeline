import ftplib
import zipfile
import os

from dotenv import load_dotenv

load_dotenv() 

hostname = f"{os.getenv('DPL_HOSTNAME')}"
username = f"{os.getenv('DPL_USERNAME')}"
password = f"{os.getenv('DPL_PASSWORD')}"
filename = f"{os.getenv('DPL_FILENAME')}"

ftp_server = ftplib.FTP(host=hostname, user=username,passwd=password)
 
# force UTF-8 encoding
ftp_server.encoding = "utf-8"   


# Write file in binary mode
with open(file=filename,mode="wb") as file:
    ftp_server.retrbinary(f"RETR {filename}", file.write)
 
# Close the Connection
ftp_server.quit()

with zipfile.ZipFile(f"{filename}","r") as zip_ref:
    zip_ref.extractall("D:\\development\\python\\DATAPIPELINEPROJECT\\extracted")

