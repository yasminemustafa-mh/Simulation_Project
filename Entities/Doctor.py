import simpy 
import numpy as np
class Doctor: 
    def __init__(self, env, number_of_doctors):
        self. env = env
        self.resource = simpy.Resource(env, capacity=number_of_doctors)

    def examine(self, patient): 
           
        print(f"Patient {patient.name} arrived at {self.env.now}")

        examination_duration = np.random.uniform(4,7)

        yield self.env.timeout(examination_duration)

        if patient.blood_pressure > 160: 
            patient.more_tests= True

        print(f"Patient {patient.name} finished at {self.env.now}")
    

