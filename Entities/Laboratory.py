import simpy 
import numpy as np

class Laboratory: 
    def __init__(self, env, number_of_stations):
        self. env = env
        self.resource = simpy.Resource(env, capacity=number_of_stations)


    def test(self, patient):     
        print(f"Patient {patient.name} arrived at {self.env.now}")

        testing_duration = np.random.uniform(3,6)

        yield self.env.timeout(testing_duration)

        print(f"Patient {patient.name} finished testing a {self.env.now}")


