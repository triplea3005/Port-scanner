#import font
import sys
#connect to node
import socket

from datetime import datetime
 
# Defining target
if len(sys.argv) == 2:
    # translating hostname to an IPv4 address
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Invalid amount of Argument")
    print("Usage: python scanner.py <host>")
    sys.exit() 

# Adding text 
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)
 
try:
    
    # scans ports between 1 - 65,535
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # returns an error indicator
        result = s.connect_ex((target ,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()
        
except KeyboardInterrupt:
        print("\n Leaving Program")
        sys.exit()
except socket.gaierror:
        print("\n Hostname could not be fixed")
        sys.exit()
except socket.error:
        print("\n Server did not respond")
        sys.exit()
