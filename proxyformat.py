import string

file = "proxys.txt"
print("Easy Proxy List Proxychains4 Formatter")
print("Leave a space after each input")
proto = input("Input Proxy Protocol:   ")
socks = proto
print("For Authenticated Proxys")
oauth = input("Enter a space then enter Username and Password. If no auth leave blank:  ")


with open(file, 'r') as fp:
    ips = [socks.join(['', x.replace(':', ' ')]) for x in fp.readlines()]
   
with open(file, 'w') as fp:
    
    fp.writelines(ips)

with open(file, 'r') as istr:
    with open('output.txt', 'w') as ostr:
        for line in istr:
            line = line.rstrip('\n') + oauth
            print(line, file=ostr)

 
print("saved as 'output.txt' Proxy list now follows Proxychains4.conf format")
print("Derek Johnston. Corexital Data")        
    
