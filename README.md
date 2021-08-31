# web-methods-collector
It's python3 script  to collect a HTTP methods allowed on the web sites,The script takes the file containing the set of subdomains, to sends an http request to each subdomain via the OPTIONS method, then prints the allowed methods for each subdomain.

# Note :
You must use the tool after crawler on your target :)

## How to use this script?

python3 options.py -f subdomains.txt

#to save the output in the file

python3 options.py -f subdomains.txt -o output.txt

## Author
Abdalla Abdelrhman Mubarak
https://www.linkedin.com/in/abdalla-abdalrhman-71b68016b/

## special thanks for:
Zahir Tariq
https://www.linkedin.com/in/zahir-tariq009/
