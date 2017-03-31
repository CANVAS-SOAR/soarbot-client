#!/usr/bin/env python3
from socket import *
import sys
import json

from CarController import CarController

def printUsage():
    print("Usage:")
    print(sys.argv[0], "[port|server:port]")

def parseArgs():
    if(2 != len(sys.argv)):
        print("Error: Invalid number of arguments")
        printUsage()
        exit(1)
    elif(sys.argv[1].isdigit()):
        port = int(sys.argv[1])
        server = "localhost"
    elif len(sys.argv[1].split(':')) == 2:
        server,port = sys.argv[1].split(':')
        if(port.isdigit()):
            port = int(port)
        else:
            print("Error: port must be an integer value");
            printUsage()
            exit(1)
    else:
        print("Error: port must be an integer value");
        printUsage()
        exit(1)

    return server,port

if __name__ == "__main__":
    server,port = parseArgs()

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((server, port))

    controller = CarController()

    while(True):
        data = s.recv(1024)

        controller.setControls(0, 1, 0, 0, 3);
        controller.setGear(0);
        data = controller.serialize()

        s.sendall(data)

