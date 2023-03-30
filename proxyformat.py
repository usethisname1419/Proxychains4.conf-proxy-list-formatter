
file = "proxys.txt"
print("Easy Proxy List Formatter - By Derek Johnston")
print("Leave a space after each input")
proto = input("Input Proxy Protocol:   ")
socks = proto

oauth = input("Enter a space then enter Username and Password. If no auth leave blank:  ")


with open(file, 'r') as fp:
    ips = [socks.join(['', x.replace(':', ' ')]) for x in fp.readlines()]

with open(file, 'w') as fp:
    ips.append(oauth)
    fp.writelines(ips)







