class Patient: 
    def __init__(self, env, name, blood_pressure, doctor, laboratory):
        self.env = env 
        self.name = name 
        self.blood_pressure = blood_pressure
        self.doctor = doctor 
        self.laboratory = laboratory
        self.more_tests = False


        
    def visit(self): 
        print("hi")
        arrival_time = self.env.now

        with self.doctor.resource.request() as req:
            yield req 
            yield self.env.process(self.doctor.examine(self))

        with self.laboratory.resource.request() as req:
            yield req 
            yield self.env.process(self.laboratory.test(self))

        process_time = self.env.now - arrival_time

        print(f"Patient {self.name} took {process_time} to finish\n")