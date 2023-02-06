import sys
sys.path.append("../lib")

import cflib.crtp
import time
import cflib.crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
from cflib.positioning.motion_commander import MotionCommander
from cflib.positioning.position_hl_commander import PositionHlCommander

#Initialisation du driver de l'antenne crazyradio
cflib.crtp.init_drivers(enable_debug_driver=False)

#Scan pour trouver drones Crazyflie
print ("Scanning interfaces for Crazyflies...")
available = cflib.crtp.scan_interfaces()
print ("Crazyflies found:")
for i in available:
    print(i[0])

#Connexion au drone Crazyflie
if len(available) > 0:
    le = cflib.crazyflie.Crazyflie(rw_cache='./cache')
    le.open_link(available[0][0])
    print("Crazyflie connected")
else:
    print("No Crazyflies not found")