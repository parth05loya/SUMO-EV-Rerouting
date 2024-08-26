#!/usr/bin/env python

import os
import sys
if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
import traci

import optparse
from sumolib import checkBinary  # Checks for the binary in environ vars
import random
#import traci
import time
import os


# we need to import some python modules from the $SUMO_HOME/tools directory

# Define the charging thresholds
threshold_low = 0.3
threshold_high = 0.8

def run():
    # Start the SUMO simulation
    sumoBinary = checkBinary('sumo-gui')  # or 'sumo-gui' for GUI version
    sumoConfig = "C:/Users/Dell/Electric_Python/electric.sumocfg"  # Replace with your actual SUMO configuration file path

    try:
        traci.start([sumoBinary, "-c", sumoConfig])
        print("TraCI started successfully")
    except Exception as e:
        print(f"Error starting TraCI: {e}")
        sys.exit(1)


    step = 0
    while step < 5000:
        traci.simulationStep()
         # type: ignore
               
       # try:
        charge_level = float(traci.vehicle.getParameter("v_0", "device.battery.actualBatteryCapacity"))
            # = traci.vehicle.getParameter("v_0", "chargeLevel")
        current_charge = charge_level
        #float(charge_level) if charge_level else 0.0
        #except ValueError:
         #   current_charge = 0.0

        time = 50 
        max_charge = 15000
        current_edge = traci.vehicle.getRoadID("v_0")
        current_route = traci.vehicle.getRouteID("v_0")
        # Check and reroute based on battery level and current edge
        if current_edge == "B4A4" and current_charge < (threshold_low * max_charge):
            traci.vehicle.setRouteID("v_0", "r_1")
            traci.vehicle.setChargingStationStop("v_0", "cs_0", duration = time )
        if current_edge == "E2":
            traci.vehicle.setParameter("v_0", "device.battery.actualBatteryCapacity", "15000")
        if current_edge == "A3A2" :
            traci.vehicle.setRouteID("v_0", "electric")
        
         
        
        
        step += 1

    traci.close()
    sys.stdout.flush()



run()   

    




