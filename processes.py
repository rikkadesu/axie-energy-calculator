class Process:
    INITIAL_ENERGY: int = 3
    INITIAL_BLOODMOON: int = 50

    def __init__(self):
        self.current_energy: int = self.INITIAL_ENERGY
        self.initial_energy = self.current_energy
        self.current_bloodmoon_damage = self.INITIAL_BLOODMOON
        self.energy_used: int = 0
        self.energy_gained: int = 0
        self.energy_destroyed: int = 0

        self.round_counter = 1
        self.current_round = f"Round {self.round_counter}"
        self.energy_history: dict = {}

    def increment_energy_used(self):
        if self.energy_used != 10 and self.current_energy != 0:
            self.energy_used += 1
            self.current_energy -= 1
            # print("Add: Used")

    def decrement_energy_used(self):
        if self.energy_used != 0:
            self.energy_used -= 1
            self.current_energy += 1
            # print("Subtract: Used")

    def increment_energy_gained(self):
        if self.energy_gained != 10:
            self.energy_gained += 1
            self.current_energy += 1
            # print("Add: Gained")

    def decrement_energy_gained(self):
        if self.energy_gained != 0:
            self.energy_gained -= 1
            self.current_energy -= 1
            # print("Subtract: Gained")

    def increment_energy_destroyed(self):
        if self.energy_destroyed != 10 and self.current_energy != 0:
            self.energy_destroyed += 1
            self.current_energy -= 1
            # print("Add: Destroyed")

    def decrement_energy_destroyed(self):
        if self.energy_destroyed != 0:
            self.energy_destroyed -= 1
            self.current_energy += 1
            # print("Subtract: Destroyed")

    def go_next_turn(self):
        self.energy_history[self.current_round] = self.initial_energy
        self.energy_used = self.energy_gained = self.energy_destroyed = 0
        self.current_round = self.current_round.replace(str(self.round_counter), str(self.round_counter + 1))
        self.round_counter += 1
        self.current_energy += 2
        if self.current_energy > 10:
            self.current_energy = 10
        if self.round_counter > 10:
            self.current_bloodmoon_damage += 30
            # print(self.current_bloodmoon_damage)
        self.initial_energy = self.current_energy
        # print(f"Round: {self.current_round}")
        # print(f"History: {self.energy_history}")
        # print(f"Current Energy: {self.current_energy}")

    def go_last_turn(self):
        if self.round_counter != 1:
            self.current_round = self.current_round.replace(str(self.round_counter), str(self.round_counter - 1))
            self.round_counter -= 1
            self.current_energy = self.energy_history[self.current_round]
            self.initial_energy = self.current_energy
        if self.round_counter > 9:
            self.current_bloodmoon_damage -= 30
        # print(f"History: {self.energy_history}")
        # print(f"Current Energy: {self.current_energy}")

    def go_restart(self):
        self.energy_used = self.energy_gained = self.energy_destroyed = 0
        self.current_energy = self.initial_energy = self.INITIAL_ENERGY
        self.current_bloodmoon_damage = self.INITIAL_BLOODMOON
        self.round_counter = 1
        self.current_round = f"Round {self.round_counter}"
        self.energy_history = {}
        # print("Restarted")