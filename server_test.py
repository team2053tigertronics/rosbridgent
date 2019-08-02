from networktables import NetworkTables

if __name__ == "__main__":
    NetworkTables.startServer(persistFilename='networktables.ini', listenAddress="127.0.0.1", port=1735)
    while(True):
        pass