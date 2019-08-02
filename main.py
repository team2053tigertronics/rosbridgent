import threading
from networktables import NetworkTables
import roslibpy

server_ip = '127.0.0.1'

cond = threading.Condition()
notified = [False]

client = None
ros_nt = None

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

def connect_to_nt_table():

    NetworkTables.initialize(server=server_ip)
    NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

    with cond:
        print("Waiting")
        if not notified[0]:
            cond.wait()

    # Insert your processing code here
    ros_nt = NetworkTables.getTable('ROS')
    print("Connected!")

def publish_to_nt_table(message):
    for key, value in message.items():
        ros_nt.putString(key, value)

if __name__ == "__main__":
    connect_to_nt_table()
    client = roslibpy.Ros(host='localhost', port=9090)
    client.run()
    print('Is ROS connected?', client.is_connected)

    listener = roslibpy.Topic(client, '/turtle_sim/', 'std_msgs/String')
    listener.subscribe(publish_to_nt_table)

    try:    
        while(client.is_connected):
            pass
    except KeyboardInterrupt:
        client.terminate()