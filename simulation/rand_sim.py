import sys
import traci


def run():
    # Simulation loop
    step = 0
    # count = traci.vehicle.getIDCount()
    routeInfo = traci.simulation.findRoute('-57827558', '30054903#1')
    traci.route.add('route1', routeInfo.edges)
    # traci.vehicle.add(vehID=veh_id,typeID='car', routeID='route1')
    veh_id = 'custom'
    print(routeInfo)



    while step < 10000:
        traci.simulationStep()
        if step == 20:
            print("creating vehicle")
            traci.vehicle.add(vehID=veh_id,typeID='trailer_1', routeID='route1')





        # Your simulation logic here
        step += 1

    # Close TraCI connection
    traci.close()
    sys.stdout.flush()


if __name__ == "__main__":
    # Connect to SUMO simulation
    traci.start(["sumo-gui", "-c", "random_sim.sumocfg"])  # opens the gui

    run()