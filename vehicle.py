class Vehicle:

    def __init__(self, vehicle_data):
        self.name = vehicle_data["name"]
        self.model = vehicle_data["model"]
        self.manufacturer = vehicle_data["manufacturer"]
        self.cost_in_credits = vehicle_data["cost_in_credits"]
        self.length = vehicle_data["length"]
        self.max_atmosphering_speed = vehicle_data["max_atmosphering_speed"]
        self.crew = vehicle_data["crew"]
        self.passengers = vehicle_data["passengers"]