import sys
sys.path.append("../lib")

import cflib.crtp
import time
import cflib.crazyflie

#Initialisation du driver de l'antenne crazyradio
cflib.crtp.init_drivers(enable_debug_driver=False)

#Scan pour trouver drones Crazyflie
print ("Scanning interfaces for Crazyflies...")
available = cflib.crtp.scan_interfaces()
print ("Crazyflies found:")
for i in available:
    print(i[0])
