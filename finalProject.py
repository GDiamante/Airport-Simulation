import random
import simpy

RANDOM_SEED = random.randint(0,10000)
NEW_AIRCRAFT = 10 #Total number of airplanes to process

# Generates aircraft and runs simulation
# @param env SimPy Environment
# @param number Number of aircraft to simulate
# @param runway The runway resource already created
def source(env, number, runway):
    aircraftInterval = 100 #how often new aircraft arrive
    aircraftSize = 100 #how many passengers on aircraft

    landingTime = 300 #how long it takes for aircraft to land
    takeoffTime = 180 #how long it takes for aircraft to takeoff
    inspectionAndRefuelTime = 1200  #how long it takes for aircraft to be inspected and refueled
    passengerCheckInTime = 15 #How long it takes for a passenger to check in

    maxDistance = 10 #maximum luggage distance (time taken to load)
    minDistance = 5 #minimum luggage distance (time taken to load)
    maxWeight = 50 #maximum luggage weight
    minWeight = 25 #minimum luggage weight
    maxSpeed = 20 #maximum passenger speed (time taken to seat)
    minSpeed = 120 #minimum passenger speed (time taken to seat)

    truckTime = random.uniform(120, 180) #time it takes for truck to deliver luggage
    maxTruckWeight = 40000 #weight the truck can hold

    randomizePassengers = True #randomize passenger seating order
    loadSeparately = False #run the inspection, luggage, and passenger loading separately
    priorityRunway = -1 #-1 for no priorities, 0 for landing priority, 2 for takeoff priority

    for i in range(number):
        luggage = generateLuggage(aircraftSize, maxDistance, minDistance, maxWeight, minWeight)
        passengers = generatePassengers(aircraftSize, maxSpeed, minSpeed, randomizePassengers)

        airCraftProcess = aircraft(
            env, 
            'Aircraft %02d' % (i + 1), 
            runway, 
            luggage, 
            passengers, 
            landingTime, 
            takeoffTime, 
            inspectionAndRefuelTime, 
            truckTime, 
            maxTruckWeight, 
            passengerCheckInTime,
            loadSeparately,
            priorityRunway)

        env.process(airCraftProcess)

        # Times out to wait for new aircraft to arrive
        t = random.expovariate(1.0 / aircraftInterval)
        yield env.timeout(t)

# Generates aircraft and runs simulation
# @param env SimPy Environment
# @param number Number of aircraft to simulate
# @param runway The runway resource already created
def sourceTwo(env, number, runway):
    aircraftInterval = 100 #how often new aircraft arrive
    aircraftSize = 200 #how many passengers on aircraft

    landingTime = 300 #how long it takes for aircraft to land
    takeoffTime = 180 #how long it takes for aircraft to takeoff
    inspectionAndRefuelTime = 1200  #how long it takes for aircraft to be inspected and refueled
    passengerCheckInTime = 15 #How long it takes for a passenger to check in

    maxDistance = 10 #maximum luggage distance (time taken to load)
    minDistance = 5 #minimum luggage distance (time taken to load)
    maxWeight = 50 #maximum luggage weight
    minWeight = 25 #minimum luggage weight
    maxSpeed = 20 #maximum passenger speed (time taken to seat)
    minSpeed = 120 #minimum passenger speed (time taken to seat)

    truckTime = random.uniform(120, 180) #time it takes for truck to deliver luggage
    maxTruckWeight = 40000 #weight the truck can hold

    randomizePassengers = True #randomize passenger seating order
    loadSeparately = False #run the inspection, luggage, and passenger loading separately
    priorityRunway = -1 #-1 for no priorities, 0 for landing priority, 2 for takeoff priority

    for i in range(number):
        luggage = generateLuggage(aircraftSize, maxDistance, minDistance, maxWeight, minWeight)
        passengers = generatePassengers(aircraftSize, maxSpeed, minSpeed, randomizePassengers)

        airCraftProcess = aircraft(
            env, 
            'Aircraft %02d' % (i + 1), 
            runway, 
            luggage, 
            passengers, 
            landingTime, 
            takeoffTime, 
            inspectionAndRefuelTime, 
            truckTime, 
            maxTruckWeight, 
            passengerCheckInTime,
            loadSeparately,
            priorityRunway)

        env.process(airCraftProcess)
        t = random.expovariate(1.0 / aircraftInterval)
        yield env.timeout(t)

# Generates aircraft and runs simulation
# @param env SimPy Environment
# @param number Number of aircraft to simulate
# @param runway The runway resource already created
def sourceThree(env, number, runway):
    aircraftInterval = 100 #how often new aircraft arrive
    aircraftSize = 100 #how many passengers on aircraft

    landingTime = 300 #how long it takes for aircraft to land
    takeoffTime = 180 #how long it takes for aircraft to takeoff
    inspectionAndRefuelTime = 1200  #how long it takes for aircraft to be inspected and refueled
    passengerCheckInTime = 15 #How long it takes for a passenger to check in

    maxDistance = 10 #maximum luggage distance (time taken to load)
    minDistance = 5 #minimum luggage distance (time taken to load)
    maxWeight = 50 #maximum luggage weight
    minWeight = 25 #minimum luggage weight
    maxSpeed = 20 #maximum passenger speed (time taken to seat)
    minSpeed = 120 #minimum passenger speed (time taken to seat)

    truckTime = random.uniform(120, 180) #time it takes for truck to deliver luggage
    maxTruckWeight = 40000 #weight the truck can hold

    randomizePassengers = True #randomize passenger seating order
    loadSeparately = False #run the inspection, luggage, and passenger loading separately
    priorityRunway = 0 #-1 for no priorities, 0 for landing priority, 2 for takeoff priority

    for i in range(number):
        luggage = generateLuggage(aircraftSize, maxDistance, minDistance, maxWeight, minWeight)
        passengers = generatePassengers(aircraftSize, maxSpeed, minSpeed, randomizePassengers)

        airCraftProcess = aircraft(
            env, 
            'Aircraft %02d' % (i + 1), 
            runway, 
            luggage, 
            passengers, 
            landingTime, 
            takeoffTime, 
            inspectionAndRefuelTime, 
            truckTime, 
            maxTruckWeight, 
            passengerCheckInTime,
            loadSeparately,
            priorityRunway)

        env.process(airCraftProcess)
        t = random.expovariate(1.0 / aircraftInterval)
        yield env.timeout(t)

# Generates aircraft and runs simulation
# @param env SimPy Environment
# @param number Number of aircraft to simulate
# @param runway The runway resource already created
def sourceFour(env, number, runway):
    aircraftInterval = 100 #how often new aircraft arrive
    aircraftSize = 100 #how many passengers on aircraft

    landingTime = 300 #how long it takes for aircraft to land
    takeoffTime = 180 #how long it takes for aircraft to takeoff
    inspectionAndRefuelTime = 1200  #how long it takes for aircraft to be inspected and refueled
    passengerCheckInTime = 15 #How long it takes for a passenger to check in

    maxDistance = 10 #maximum luggage distance (time taken to load)
    minDistance = 5 #minimum luggage distance (time taken to load)
    maxWeight = 50 #maximum luggage weight
    minWeight = 25 #minimum luggage weight
    maxSpeed = 20 #maximum passenger speed (time taken to seat)
    minSpeed = 120 #minimum passenger speed (time taken to seat)

    truckTime = random.uniform(120, 180) #time it takes for truck to deliver luggage
    maxTruckWeight = 40000 #weight the truck can hold

    randomizePassengers = True #randomize passenger seating order
    loadSeparately = False #run the inspection, luggage, and passenger loading separately
    priorityRunway = 2 #-1 for no priorities, 0 for landing priority, 2 for takeoff priority

    for i in range(number):
        luggage = generateLuggage(aircraftSize, maxDistance, minDistance, maxWeight, minWeight)
        passengers = generatePassengers(aircraftSize, maxSpeed, minSpeed, randomizePassengers)

        airCraftProcess = aircraft(
            env, 
            'Aircraft %02d' % (i + 1), 
            runway, 
            luggage, 
            passengers, 
            landingTime, 
            takeoffTime, 
            inspectionAndRefuelTime, 
            truckTime, 
            maxTruckWeight, 
            passengerCheckInTime,
            loadSeparately,
            priorityRunway)

        env.process(airCraftProcess)
        t = random.expovariate(1.0 / aircraftInterval)
        yield env.timeout(t)

# Generates aircraft and runs simulation
# @param env SimPy Environment
# @param number Number of aircraft to simulate
# @param runway The runway resource already created
def sourceFive(env, number, runway):
    aircraftInterval = 100 #how often new aircraft arrive
    aircraftSize = 100 #how many passengers on aircraft

    landingTime = 300 #how long it takes for aircraft to land
    takeoffTime = 180 #how long it takes for aircraft to takeoff
    inspectionAndRefuelTime = 1200  #how long it takes for aircraft to be inspected and refueled
    passengerCheckInTime = 15 #How long it takes for a passenger to check in

    maxDistance = 10 #maximum luggage distance (time taken to load)
    minDistance = 5 #minimum luggage distance (time taken to load)
    maxWeight = 50 #maximum luggage weight
    minWeight = 25 #minimum luggage weight
    maxSpeed = 20 #maximum passenger speed (time taken to seat)
    minSpeed = 120 #minimum passenger speed (time taken to seat)

    truckTime = random.uniform(120, 180) #time it takes for truck to deliver luggage
    maxTruckWeight = 40000 #weight the truck can hold

    randomizePassengers = True #randomize passenger seating order
    loadSeparately = True #run the inspection, luggage, and passenger loading separately
    priorityRunway = -1 #-1 for no priorities, 0 for landing priority, 2 for takeoff priority

    for i in range(number):
        luggage = generateLuggage(aircraftSize, maxDistance, minDistance, maxWeight, minWeight)
        passengers = generatePassengers(aircraftSize, maxSpeed, minSpeed, randomizePassengers)

        airCraftProcess = aircraft(
            env, 
            'Aircraft %02d' % (i + 1), 
            runway, 
            luggage, 
            passengers, 
            landingTime, 
            takeoffTime, 
            inspectionAndRefuelTime, 
            truckTime, 
            maxTruckWeight, 
            passengerCheckInTime,
            loadSeparately,
            priorityRunway)

        env.process(airCraftProcess)
        t = random.expovariate(1.0 / aircraftInterval)
        yield env.timeout(t)

# Generates aircraft and runs simulation
# @param env SimPy Environment
# @param number Number of aircraft to simulate
# @param runway The runway resource already created
def sourceSix(env, number, runway):
    aircraftInterval = 100 #how often new aircraft arrive
    aircraftSize = 100 #how many passengers on aircraft

    landingTime = 100 #how long it takes for aircraft to land
    takeoffTime = 50 #how long it takes for aircraft to takeoff
    inspectionAndRefuelTime = 1200  #how long it takes for aircraft to be inspected and refueled
    passengerCheckInTime = 15 #How long it takes for a passenger to check in

    maxDistance = 10 #maximum luggage distance (time taken to load)
    minDistance = 5 #minimum luggage distance (time taken to load)
    maxWeight = 50 #maximum luggage weight
    minWeight = 25 #minimum luggage weight
    maxSpeed = 20 #maximum passenger speed (time taken to seat)
    minSpeed = 120 #minimum passenger speed (time taken to seat)

    truckTime = random.uniform(120, 180) #time it takes for truck to deliver luggage
    maxTruckWeight = 40000 #weight the truck can hold

    randomizePassengers = True #randomize passenger seating order
    loadSeparately = False #run the inspection, luggage, and passenger loading separately
    priorityRunway = -1 #-1 for no priorities, 0 for landing priority, 2 for takeoff priority

    for i in range(number):
        luggage = generateLuggage(aircraftSize, maxDistance, minDistance, maxWeight, minWeight)
        passengers = generatePassengers(aircraftSize, maxSpeed, minSpeed, randomizePassengers)

        airCraftProcess = aircraft(
            env, 
            'Aircraft %02d' % (i + 1), 
            runway, 
            luggage, 
            passengers, 
            landingTime, 
            takeoffTime, 
            inspectionAndRefuelTime, 
            truckTime, 
            maxTruckWeight, 
            passengerCheckInTime,
            loadSeparately,
            priorityRunway)

        env.process(airCraftProcess)
        t = random.expovariate(1.0 / aircraftInterval)
        yield env.timeout(t)

# Generates aircraft and runs simulation
# @param env SimPy Environment
# @param number Number of aircraft to simulate
# @param runway The runway resource already created
def sourceSeven(env, number, runway):
    aircraftInterval = 100 #how often new aircraft arrive
    aircraftSize = 100 #how many passengers on aircraft

    landingTime = 300 #how long it takes for aircraft to land
    takeoffTime = 180 #how long it takes for aircraft to takeoff
    inspectionAndRefuelTime = 1200  #how long it takes for aircraft to be inspected and refueled
    passengerCheckInTime = 5 #How long it takes for a passenger to check in

    maxDistance = 5 #maximum luggage distance (time taken to load)
    minDistance = 2 #minimum luggage distance (time taken to load)
    maxWeight = 50 #maximum luggage weight
    minWeight = 25 #minimum luggage weight
    maxSpeed = 5 #maximum passenger speed (time taken to seat)
    minSpeed = 50 #minimum passenger speed (time taken to seat)

    truckTime = random.uniform(120, 180) #time it takes for truck to deliver luggage
    maxTruckWeight = 40000 #weight the truck can hold

    randomizePassengers = True #randomize passenger seating order
    loadSeparately = False #run the inspection, luggage, and passenger loading separately
    priorityRunway = -1 #-1 for no priorities, 0 for landing priority, 2 for takeoff priority

    for i in range(number):
        luggage = generateLuggage(aircraftSize, maxDistance, minDistance, maxWeight, minWeight)
        passengers = generatePassengers(aircraftSize, maxSpeed, minSpeed, randomizePassengers)

        airCraftProcess = aircraft(
            env, 
            'Aircraft %02d' % (i + 1), 
            runway, 
            luggage, 
            passengers, 
            landingTime, 
            takeoffTime, 
            inspectionAndRefuelTime, 
            truckTime, 
            maxTruckWeight, 
            passengerCheckInTime,
            loadSeparately,
            priorityRunway)

        env.process(airCraftProcess)
        t = random.expovariate(1.0 / aircraftInterval)
        yield env.timeout(t)

# Generates aircraft and runs simulation
# @param env SimPy Environment
# @param number Number of aircraft to simulate
# @param runway The runway resource already created
def sourceEight(env, number, runway):
    aircraftInterval = 100 #how often new aircraft arrive
    aircraftSize = 100 #how many passengers on aircraft

    landingTime = 100 #how long it takes for aircraft to land
    takeoffTime = 50 #how long it takes for aircraft to takeoff
    inspectionAndRefuelTime = 1200  #how long it takes for aircraft to be inspected and refueled
    passengerCheckInTime = 15 #How long it takes for a passenger to check in

    maxDistance = 10 #maximum luggage distance (time taken to load)
    minDistance = 5 #minimum luggage distance (time taken to load)
    maxWeight = 50 #maximum luggage weight
    minWeight = 25 #minimum luggage weight
    maxSpeed = 20 #maximum passenger speed (time taken to seat)
    minSpeed = 120 #minimum passenger speed (time taken to seat)

    truckTime = random.uniform(120, 180) #time it takes for truck to deliver luggage
    maxTruckWeight = 40000 #weight the truck can hold

    randomizePassengers = True #randomize passenger seating order
    loadSeparately = False #run the inspection, luggage, and passenger loading separately
    priorityRunway = 0 #-1 for no priorities, 0 for landing priority, 2 for takeoff priority

    for i in range(number):
        luggage = generateLuggage(aircraftSize, maxDistance, minDistance, maxWeight, minWeight)
        passengers = generatePassengers(aircraftSize, maxSpeed, minSpeed, randomizePassengers)

        airCraftProcess = aircraft(
            env, 
            'Aircraft %02d' % (i + 1), 
            runway, 
            luggage, 
            passengers, 
            landingTime, 
            takeoffTime, 
            inspectionAndRefuelTime, 
            truckTime, 
            maxTruckWeight, 
            passengerCheckInTime,
            loadSeparately,
            priorityRunway)

        env.process(airCraftProcess)
        t = random.expovariate(1.0 / aircraftInterval)
        yield env.timeout(t)

# Generates aircraft and runs simulation
# @param env SimPy Environment
# @param number Number of aircraft to simulate
# @param runway The runway resource already created
def sourceNine(env, number, runway):
    aircraftInterval = 100 #how often new aircraft arrive
    aircraftSize = 100 #how many passengers on aircraft

    landingTime = 100 #how long it takes for aircraft to land
    takeoffTime = 50 #how long it takes for aircraft to takeoff
    inspectionAndRefuelTime = 1200  #how long it takes for aircraft to be inspected and refueled
    passengerCheckInTime = 15 #How long it takes for a passenger to check in

    maxDistance = 10 #maximum luggage distance (time taken to load)
    minDistance = 5 #minimum luggage distance (time taken to load)
    maxWeight = 50 #maximum luggage weight
    minWeight = 25 #minimum luggage weight
    maxSpeed = 20 #maximum passenger speed (time taken to seat)
    minSpeed = 120 #minimum passenger speed (time taken to seat)

    truckTime = random.uniform(120, 180) #time it takes for truck to deliver luggage
    maxTruckWeight = 40000 #weight the truck can hold

    randomizePassengers = True #randomize passenger seating order
    loadSeparately = False #run the inspection, luggage, and passenger loading separately
    priorityRunway = 2 #-1 for no priorities, 0 for landing priority, 2 for takeoff priority

    for i in range(number):
        luggage = generateLuggage(aircraftSize, maxDistance, minDistance, maxWeight, minWeight)
        passengers = generatePassengers(aircraftSize, maxSpeed, minSpeed, randomizePassengers)

        airCraftProcess = aircraft(
            env, 
            'Aircraft %02d' % (i + 1), 
            runway, 
            luggage, 
            passengers, 
            landingTime, 
            takeoffTime, 
            inspectionAndRefuelTime, 
            truckTime, 
            maxTruckWeight, 
            passengerCheckInTime,
            loadSeparately,
            priorityRunway)

        env.process(airCraftProcess)
        t = random.expovariate(1.0 / aircraftInterval)
        yield env.timeout(t)

# Generates aircraft and runs simulation
# @param env SimPy Environment
# @param number Number of aircraft to simulate
# @param runway The runway resource already created
def sourceTen(env, number, runway):
    aircraftInterval = 100 #how often new aircraft arrive
    aircraftSize = 100 #how many passengers on aircraft

    landingTime = 100 #how long it takes for aircraft to land
    takeoffTime = 50 #how long it takes for aircraft to takeoff
    inspectionAndRefuelTime = 1200  #how long it takes for aircraft to be inspected and refueled
    passengerCheckInTime = 15 #How long it takes for a passenger to check in

    maxDistance = 10 #maximum luggage distance (time taken to load)
    minDistance = 5 #minimum luggage distance (time taken to load)
    maxWeight = 50 #maximum luggage weight
    minWeight = 25 #minimum luggage weight
    maxSpeed = 20 #maximum passenger speed (time taken to seat)
    minSpeed = 120 #minimum passenger speed (time taken to seat)

    truckTime = random.uniform(120, 180) #time it takes for truck to deliver luggage
    maxTruckWeight = 40000 #weight the truck can hold

    randomizePassengers = True #randomize passenger seating order
    loadSeparately = True #run the inspection, luggage, and passenger loading separately
    priorityRunway = -1 #-1 for no priorities, 0 for landing priority, 2 for takeoff priority

    for i in range(number):
        luggage = generateLuggage(aircraftSize, maxDistance, minDistance, maxWeight, minWeight)
        passengers = generatePassengers(aircraftSize, maxSpeed, minSpeed, randomizePassengers)

        airCraftProcess = aircraft(
            env, 
            'Aircraft %02d' % (i + 1), 
            runway, 
            luggage, 
            passengers, 
            landingTime, 
            takeoffTime, 
            inspectionAndRefuelTime, 
            truckTime, 
            maxTruckWeight, 
            passengerCheckInTime,
            loadSeparately,
            priorityRunway)

        env.process(airCraftProcess)
        t = random.expovariate(1.0 / aircraftInterval)
        yield env.timeout(t)

# Processes the aircraft's actions
# @param env SimPy Environment
# @param name Name of the aircraft being processed
# @param runway The runway resource already created
# @param luggage Array of dicts, contains luggage information
# @param passengers Array of dicts, contains passenger information
# @param landingTime Number of seconds it takes an aircraft to land
# @param takeoffTime Number of seconds it takes an aircraft to takeoff
# @param inspectionAndRefuelTime Number of seconds it takes an aircraft to be inspected and refueled
# @param truckTime Number of seconds it takes the truck to deliver luggage
# @param maxTruckWeight Amount of luggage weight the truck can hold
# @param passengerCheckInTime Length of time it takes a passenger to check in
# @param loadSeparately Boolean if true loads passengers, luggage, and inspection at different times
# @param priorityRunway -1 for no priorities, 0 for landing priority, 2 for takeoff priority
def aircraft(env, name, runway, luggage, passengers, landingTime, takeoffTime, inspectionAndRefuelTime, truckTime, maxTruckWeight, passengerCheckInTime, loadSeparately, priorityRunway):
    
    # Set the landing request to the passed in priority if positive
    if priorityRunway >= 0:
        req = runway.request(priority = priorityRunway)
    else:
        req = runway.request()

    print('RUNWAY REQUEST ' + name, env.now)
    # Wait for runway
    yield req

    print('LANDING ' + name, env.now)
    yield env.process(landPlane(env, landingTime))
    print('LANDED ' + name, env.now)

    # Free up the runway
    runway.release(req)

    print('LOADING ' + name, env.now)
    # Perform the inspection, luggage loading and passenger loading
    yield env.process(loadingSequence(env, inspectionAndRefuelTime, luggage, truckTime, maxTruckWeight, passengers, passengerCheckInTime, loadSeparately))
    print('DONE LOADING ' + name, env.now)

    # Request runway for take off
    # If the priority has been set to 2, set takeoff priority to zero so it has priority
    # If the priority has been set to 0, set takeoff priority to two so landing has priority
    # If priority is anything else assume theres no priority
    if priorityRunway == 2:
        req2 = runway.request(priority = 0)
    elif priorityRunway == 0:
        req2 = runway.request(priority = 2)
    else:
        req2 = runway.request()
    print('TAKEOFF REQUEST ' + name, env.now)
    # Wait for runway
    yield req2
    print('TAKING OFF ' + name, env.now)
    yield env.process(takeoffPlane(env, takeoffTime))
    print('TOOK OFF ' + name, env.now)
    # Free up runway
    runway.release(req2)

# Operation to land the aircraft
# @param env SimPy Environment
# @param duration length of time to land
def landPlane(env, duration):
    yield env.timeout(duration)

# Operation to takeoff the aircraft
# @param env SimPy Environment
# @param duration length of time to takeoff
def takeoffPlane(env, duration):
    yield env.timeout(duration)

# Processes the different loading operations
# @param env SimPy Environment
# @param inspectionAndRefuelTime Number of seconds it takes an aircraft to be inspected and refueled
# @param luggage Array of dicts, contains luggage information
# @param truckTime Number of seconds it takes the truck to deliver luggage
# @param maxTruckWeight Amount of luggage weight the truck can hold
# @param passengers Array of dicts, contains passenger information
# @param passengerCheckInTime Length of time it takes a passenger to check in
# @param loadSeparately Boolean if true loads passengers, luggage, and inspection at different times
def loadingSequence(env, inspectionAndRefuelTime, luggage, truckTime, maxTruckWeight, passengers, passengerCheckInTime, loadSeparately):
    if loadSeparately:
        yield env.process(inspectAndRefuel(env, inspectionAndRefuelTime))
        yield env.process(loadLuggage(env, luggage, truckTime, maxTruckWeight))
        yield env.process(boardPassengers(env, passengers, passengerCheckInTime))
    else:
        yield (
            env.process(inspectAndRefuel(env, inspectionAndRefuelTime)) &
            env.process(loadLuggage(env, luggage, truckTime, maxTruckWeight)) &
            env.process(boardPassengers(env, passengers, passengerCheckInTime)))

# Processes the different loading operations
# @param env SimPy Environment
# @param duration length of time to inspect and refuel
def inspectAndRefuel(env, duration):
    yield env.timeout(duration)

# Processes the different loading operations
# @param env SimPy Environment
# @param luggage Array of dicts, contains luggage information
# @param truckTime Number of seconds it takes the truck to deliver luggage
# @param maxTruckWeight Amount of luggage weight the truck can hold
def loadLuggage(env, luggage, truckTime, maxTruckWeight):
    truckWeight = 0

    for bag in luggage:
        # Wait for the truck to drive if it has been filled up
        if (bag['weight'] + truckWeight) > maxTruckWeight:
            yield env.timeout(truckTime)
            truckWeight = 0
        yield env.timeout(bag['distance'])
        truckWeight += bag['weight']

    yield env.timeout((truckTime))

# Processes the different loading operations
# @param env SimPy Environment
# @param passengers Array of dicts, contains passenger information
# @param passengerCheckInTime Length of time it takes a passenger to check in
def boardPassengers(env, passengers, passengerCheckInTime):
    for passenger in passengers:
        yield env.timeout(passengerCheckInTime)
        passenger['status'] = env.timeout(passenger['speed'])

    # Wait for all passengers to have seated
    for passenger in passengers:
        yield passenger['status']

# Generates all of the passenger's luggage
# @param aircraftSize number of seats on aircraft
# @param maxDistance maximum length of time it takes to load a single piece of luggage
# @param minDistance minimum length of time it takes to load a single piece of luggage
# @param maxWeight maximum weight a piece of luggage can weigh
# @param minWeight minimum weight a piece of luggage can weigh
def generateLuggage(aircraftSize, maxDistance, minDistance, maxWeight, minWeight):
    luggage = [None] * aircraftSize
    for x in range(aircraftSize):
        luggage[x] = {
            'index': x,
            'distance': random.uniform(minDistance, maxDistance),
            'weight': random.uniform(minWeight, maxWeight)
        }
    return luggage

# Generates all of the passenger's luggage
# @param aircraftSize number of seats on aircraft
# @param maxSpeed maximum amount of time it takes for a passenger to board
# @param minSpeed minimum amount of time it takes for a passenger to board
# @param radomize if true randomizes the ordering of passengers
def generatePassengers(airCraftSize, maxSpeed, minSpeed, randomize):
    passengers = [None] * airCraftSize
    for x in range(airCraftSize):
        passengers[x] = {
            'seatNumber': x + 1,
            'speed': random.uniform(minSpeed, maxSpeed),
        }
    if randomize:
        random.shuffle(passengers)
    return passengers

random.seed(RANDOM_SEED)

# Setup and start the simulation
print('#####################First Airport Simulating##################################')
env = simpy.Environment()

runway = simpy.Resource(env, capacity=1)

env.process(source(env, NEW_AIRCRAFT, runway))
env.run()
sourceOneTime = env.now

# Setup and start the simulation
print('\n\n#####################Second Airport Simulating##################################\n')
env = simpy.Environment()

runway = simpy.Resource(env, capacity=1)

env.process(sourceTwo(env, NEW_AIRCRAFT, runway))
env.run()
sourceTwoTime = env.now

# Setup and start the simulation
print('\n\n#####################Third Airport Simulating##################################\n')
env = simpy.Environment()

runway = simpy.PriorityResource(env, capacity=1)

env.process(sourceThree(env, NEW_AIRCRAFT, runway))
env.run()
sourceThreeTime = env.now

# Setup and start the simulation
print('\n\n#####################Fourth Airport Simulating##################################\n')
env = simpy.Environment()

runway = simpy.PriorityResource(env, capacity=1)

env.process(sourceFour(env, NEW_AIRCRAFT, runway))
env.run()
sourceFourTime = env.now

# Setup and start the simulation
print('\n\n#####################Fifth Airport Simulating##################################\n')
env = simpy.Environment()

runway = simpy.Resource(env, capacity=1)

env.process(sourceFive(env, NEW_AIRCRAFT, runway))
env.run()
sourceFiveTime = env.now

# Setup and start the simulation
print('\n\n#####################Sixth Airport Simulating##################################\n')
env = simpy.Environment()

runway = simpy.Resource(env, capacity=1)

env.process(sourceSix(env, NEW_AIRCRAFT, runway))
env.run()
sourceSixTime = env.now

# Setup and start the simulation
print('\n\n#####################Seventh Airport Simulating##################################\n')
env = simpy.Environment()

runway = simpy.Resource(env, capacity=1)

env.process(sourceSeven(env, NEW_AIRCRAFT, runway))
env.run()
sourceSevenTime = env.now

# Setup and start the simulation
print('\n\n#####################Eighth Airport Simulating##################################\n')
env = simpy.Environment()

runway = simpy.PriorityResource(env, capacity=1)

env.process(sourceEight(env, NEW_AIRCRAFT, runway))
env.run()
sourceEightTime = env.now

# Setup and start the simulation
print('\n\n#####################Ninth Airport Simulating##################################\n')
env = simpy.Environment()

runway = simpy.PriorityResource(env, capacity=1)

env.process(sourceNine(env, NEW_AIRCRAFT, runway))
env.run()
sourceNineTime = env.now

# Setup and start the simulation
print('\n\n#####################Tenth Airport Simulating##################################\n')
env = simpy.Environment()

runway = simpy.Resource(env, capacity=1)

env.process(sourceTen(env, NEW_AIRCRAFT, runway))
env.run()
sourceTenTime = env.now

print("\n\nFINAL TIMES")
print("Simulation One Time:   ", sourceOneTime)
print("Simulation Two Time:   ", sourceTwoTime)
print("Simulation Three Time: ", sourceThreeTime)
print("Simulation Four Time:  ", sourceFourTime)
print("Simulation Five Time:  ", sourceFiveTime)
print("Simulation Six Time:   ", sourceSixTime)
print("Simulation Seven Time: ", sourceSevenTime)
print("Simulation Eight Time: ", sourceEightTime)
print("Simulation Nine Time:  ", sourceNineTime)
print("Simulation Ten Time:  ", sourceTenTime)