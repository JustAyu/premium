# Credit Goes To Ayush!

import os
from dotenv import load_dotenv, find_dotenv, set_key
load_dotenv(find_dotenv())


print("Give these vars carefully: \n")
set_key('.env','API_ID', input("API_ID : "))
set_key('.env','API_HASH', input("API_HASH : "))
set_key('.env','OWNER_ID', input("OWNER_ID : "))