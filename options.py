import requests 
import threading
from colorama import Fore
import argparse

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",help="subdomains OR urls file", required=True)
parser.add_argument("-o","--output",help="output file", required=False)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
args = parser.parse_args()

results = []
def run_requests(sub):
    try:
        response = requests.options(sub)
        headers = response.headers
        if "Allow" in headers:
            print(Fore.GREEN+ sub+ ' ==> ' +headers['Allow'])
            results.append(sub + ' ==> ' + headers['Allow'])

        else:
            None
    except Exception:
        print(Fore.RED+"Check your internet connection")


def main():

    subs_list = (str(args.file)).strip()

    list_of_thread = []

    with open(subs_list,'r') as file:
        for sub in file:
            sub = sub.strip()
            new_threading = threading.Thread(target=run_requests,args=[sub])
            new_threading.start()
            list_of_thread.append(new_threading)

        for thread in list_of_thread:
            thread.join()



if __name__ == '__main__':
    main()

# output file
anaconda = open(str(args.output),'w+')
for item in results:
    anaconda.write(str(item))
    anaconda.write('\n')
anaconda.close()

