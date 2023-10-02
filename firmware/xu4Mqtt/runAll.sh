#!/bin/bash
sleep 60

kill $(pgrep -f 'python3 ips7100ReaderV2.py')
sleep 5
python3 ips7100ReaderV2.py 0 &
sleep 5

kill $(pgrep -f 'python3 i2cReader.py')
sleep 5
python3 i2cReader.py &
sleep 5

python3 ipReader.py
sleep 5

kill $(pgrep -f 'python3 audioReader.py')
sleep 5
cd /home/teamlary/gitHubRepos/indoorTestNode/firmware/xu4Mqtt && /home/teamlary/birdSongs/bin/python3 audioReader.py

