#import urllib
#use urllib.request to get the data from url
#write a function that takes a url
#return a response


import urllib.request as urllib_request



def main(url):
    print("Checking connectivity...")
    try:

        response = urllib_request.urlopen(url)
        print(f"Connected to {url} successfully")
        print(f"The response code was: {response.getcode()}")
    except:
        print(f"Error. Is not possible connect to {url}")

def init():
    print("SITE CONNECTIVITY CHECKER")
    input_url = input("Input the URL to check: ")
    main(input_url)

if __name__ == '__main__':
    init()