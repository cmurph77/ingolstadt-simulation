# this will be done by generating vehicles with traci
import sys
import traci
import random

route_count = 1
veh_count = 1
start_edges = [ '-118607485','-672008260#1','-217272033','-472368151','-23623780#2']
# end_edges   = [ '118607485','672008260#1','217272033','472368151','23623780#2']   -- inverse of start
end_edges = ['173178641','93112169#3','-25188979#1','42276507']

def insert_vehicle(route_edges):
    global route_count, veh_count  # Declare these variables as global
    traci.route.add(str(route_count), route_edges)
    traci.vehicle.add(vehID=str(veh_count), routeID=str(route_count))
    route_count =  route_count + 1
    veh_count = veh_count + 1

def get_route(start_e,end_e):
    routeInfo = traci.simulation.findRoute(start_e,end_e)
    return routeInfo.edges


def run():
    start_edges = [ '-118607485','-672008260#1','-217272033','-472368151','-23623780#2']
    end_edges = ['173178641','93112169#3','-25188979#1','42276507']
    # Simulation loop
    step = 0

    while True:
        traci.simulationStep()
        if step  % 10 == 0:
            print("Inserting vehicle")
            route = get_route(random.choice(start_edges),random.choice(end_edges))
            insert_vehicle(route_edges=route)

        # Your simulation logic here
        step += 1

    # Close TraCI connection
    traci.close()
    sys.stdout.flush()


if __name__ == "__main__":
    # Connect to SUMO simulation
    traci.start(["sumo-gui", "-c", "random_sim.sumocfg"])  # opens the gui

    run()