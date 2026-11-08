import numpy as np

import simpy 
from Entities.Doctor import Doctor 
from Entities.Laboratory import Laboratory
from Entities.Patient import Patient


def generate_patients(env, doctor, laboratory): 

    for i in range(1,11): 

        time_btwn_arrivals = np.random.exponential(scale=3)

        yield env.timeout(time_btwn_arrivals)

        blood_pressure = np.random.randint(90,200)

        patient = Patient(env, "Patient#"+ str(i), blood_pressure, doctor, laboratory)

        env.process(patient.visit())
       



env = simpy.Environment()

lab = Laboratory(env,number_of_stations=1)
doctor = Doctor(env, number_of_doctors=1)

env.process(generate_patients(env, doctor, lab))

env.run()

