#import OS to allow for interaction with environment variables in the operating system
import os

#create class ro hold config data for web service class Config:
class Config:
    #define secret key
    SECRET_KEY = os.environ.get ('SECRET_KEY') or "Y9HF63HUF"
