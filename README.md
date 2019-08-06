# rosbridgent
Connects rosbridge to nt

Instructions to get up and running:

1. sudo apt-get install sudo apt-get install ros-kinetic-rosbridge-server
2. source /opt/ros/kinetic/setup.bash
3. git clone https://github.com/wpilibsuite/OutlineViewer.git
4. cd OutlineViewer
5. ./gradlew build
6. ./gradlew run
7. git clone https://github.com/team2053tigertronics/rosbridgent.git
8. cd rosbridgent
9. python3 -m venv ./venv
10. source venv/bin/activate
11. pip3 install -r requirements.txt
12. python3 main.py
13. roslaunch rosbridge_server rosbridge_websocket.launch

You should see a list of ros nodes on outline viewer.
