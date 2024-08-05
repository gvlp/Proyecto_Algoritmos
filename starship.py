class Starship:

    def __init__(self, starship_data):
        self.name = starship_data["name"]
        self.model = starship_data["model"]
        self.manufacturer = starship_data["manufacturer"]
        self.cost_in_credits = starship_data["cost_in_credits"]
        self.length = starship_data["length"]
        self.max_atmosphering_speed = starship_data["max_atmosphering_speed"]
        self.crew = starship_data["crew"]
        self.passengers = starship_data["passengers"]