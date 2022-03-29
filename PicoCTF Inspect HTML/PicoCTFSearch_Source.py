import requests#interfaces with the webpage
import re#regular expression to find the flag

def searchSource():

    url = "http://saturn.picoctf.net:59430/"  # location of the challenge

    r = requests.get(url)#we grab the page that we recieved after sending the desired packet w/ headers

    flag = re.findall("picoCTF{.*}", r.text)#and search it for the flag, which shows up as picoCTF{Flag_text_here}

    print(flag)#print the found flag


searchSource()#and call the function to run the method