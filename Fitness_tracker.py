class Fitness_tracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0
    def add_steps(self,steps):
        self.steps+=steps
        self.calories+=steps*0.04
    def show_data(self):
        print("steps walked:",self.steps)
        print("calories burned:",self.calories)
tracker = Fitness_tracker()
tracker.add_steps(2000)
tracker.add_steps(1500)
tracker.show_data()                