file = "proxys.txt"
socks = "socks5  "

oauth = input("Enter Username and Password. If no auth leave blank:  ")

with open(file, 'r') as fp:
    ips = [socks.join(['', x.replace(':', ' '), oauth]) for x in fp.readlines()]

with open(file, 'w') as fp:
    fp.writelines(ips)
