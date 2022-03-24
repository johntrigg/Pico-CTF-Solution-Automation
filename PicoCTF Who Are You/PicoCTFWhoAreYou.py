import requests#interfaces with the webpage
import re#regular expression to find the flag

def whoAreYou():
    url = "http://mercury.picoctf.net:46199/" #location of the challenge

    header = {
        "User-Agent": "PicoBrowser",
        "Referer": "http://mercury.picoctf.net:46199/",
        "Date": "2018", "Dnt": "1",
        "X-Forwarded-For": "212.107.154.192",
        "Accept-Language": "sv-SE"
    }#CTF challenge involves modifying a HTTP packet to have certain headers
    #so we use module requests to modify the packet via Python code

    r = requests.get(url, headers=header)#we grab the page that we recieved after sending the desired packet w/ headers

    flag = re.findall("picoCTF{.*}", r.text)[0]#and search it for the flag, which shows up as picoCTF{Flag_text_here}

    print(flag)#print the found flag


whoAreYou()#and call the function to run the method