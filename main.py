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

def publish_to_nt_table(message):
    print(message)
    for key, value in message.items():
        table.putString(key, value)

def publish_nodes(message):
    print(message)
    for node in message['nodes']:
        global ros_nt
        ros_nt.putString(node, "")

NetworkTables.initialize(server=server_ip)
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print("Waiting")
    if not notified[0]:
        cond.wait()
        
ros_nt = NetworkTables.getTable('ROS')
print("Connected!")
client = roslibpy.Ros(host='localhost', port=9090)
client.run()
print('Is ROS connected?', client.is_connected)
client.get_nodes(publish_nodes)
try:
    while(client.is_connected):
        pass
except KeyboardInterrupt:
    client.terminate()

#listener = roslibpy.Topic(client, 'rtabmap_ros/MapGraph', 'std_msgs/String')
#listener.subscribe(publish_to_nt_table)
