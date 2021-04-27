import sys
import socket
from datetime import datetime

# define the target by running the script in terminal (Portscanner.py 192.168.1.1 90 150)

if len(sys.argv) == 4:
    target = socket.gethostbyname(sys.argv[1])
    startport = int(sys.argv[2])
    endport = int(sys.argv[3])
else:
    # help banner
    print("-"*50)
    print("     -ip The ip address of the target. ")
    print("     -p1 The Port To Start the Scan.")
    print("     -p2 The Port To Stop the Scan.")
    print("-"*50)


def banner():
    print("-"*50)
    print("PortScanner (https://github.com/XEn0CidE) ")
    print("scanning target " + target)
    print("time started " + str(datetime.now()))
    print("-"*50)

try: 
    banner()
    for port in range(startport,endport):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if(result == 0):
            print("port {} is open".format(port))
        
except KeyboardInterrupt:
    print("\nさようなら...")
    sys.exit()
except socket.gaierror:
    print("Host name could not be Resolved")
    sys.exit
except socket.error:
    print("Could not Connect to Server")
    sys.exit
