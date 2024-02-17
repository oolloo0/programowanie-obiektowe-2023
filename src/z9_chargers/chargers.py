class Charger:
    def __init__(self, max_current_kw):
        self.max_current_kw = max_current_kw
        self.is_available = True

class ChargingService:
    def __init__(self):
        self.chargers = []
        self.charging_sessions = {}

    def add_charger(self, charger):
        self.chargers.append(charger)

    def remove_charger(self, charger):
        if charger in self.chargers:
            self.chargers.remove(charger)

    def start_charging(self, vin, desired_current_kw):
        for charger in self.chargers:
            if charger.is_available and desired_current_kw <= charger.max_current_kw:
                charger.is_available = False
                self.charging_sessions[vin] = {"current_kw": desired_current_kw, "status": "CHARGING"}
                print(f"Charging started for {vin} at {desired_current_kw} kW.")
                return
        print("No available charger or current too high.")

    def stop_charging(self, vin):
        if vin in self.charging_sessions:
            for charger in self.chargers:
                if not charger.is_available:
                    charger.is_available = True
                    break
            self.charging_sessions[vin]["status"] = "FINISHED"
            print(f"Charging stopped for {vin}.")
        else:
            print("Charging session not found.")


charging_service = ChargingService()
charger1 = Charger(22)
charger2 = Charger(11)
charging_service.add_charger(charger1)
charging_service.add_charger(charger2)

charging_service.start_charging("VIN123", 10)

charging_service.stop_charging("VIN123")


class ClientAccount:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Car:
    def __init__(self, vin, owner_id, max_current_kw):
        self.vin = vin
        self.owner_id = owner_id
        self.max_current_kw = max_current_kw

class Charger:
    def __init__(self, max_current_kw):
        self.max_current_kw = max_current_kw
        self.available = True

class ChargingService:
    def __init__(self):
        self.chargers = []
        self.clients = {}
        self.cars = {}

    def add_charger(self, charger):
        self.chargers.append(charger)

    def register_client(self, client):
        self.clients[client.id] = client

    def register_car(self, car):
        self.cars[car.vin] = car

    def start_charging(self, client_id, vin, charger_index):
        if client_id not in self.clients or vin not in self.cars:
            print("Client or car not found.")
            return False
        if charger_index >= len(self.chargers) or not self.chargers[charger_index].available:
            print("Charger not available.")
            return False
        car = self.cars[vin]
        charger = self.chargers[charger_index]
        if car.max_current_kw > charger.max_current_kw:
            print("Car's max current exceeds charger's capacity.")
            return False
        charger.available = False
        print(f"Charging started for car {vin} on charger {charger_index}.")
        return True

    def stop_charging(self, vin, charger_index):
        if charger_index >= len(self.chargers):
            print("Invalid charger index.")
            return False
        charger = self.chargers[charger_index]
        if charger.available:
            print("Charger is not in use.")
            return False
        charger.available = True
        print(f"Charging stopped for car {vin} on charger {charger_index}.")
        return True


charging_service = ChargingService()
charging_service.add_charger(Charger(22))

client = ClientAccount("1", "Janusz Wąsowicz")
car = Car("VIN123", "1", 20)


charging_service.register_client(client)
charging_service.register_car(car)


if charging_service.start_charging("1", "VIN123", 0):
    charging_service.stop_charging("VIN123", 0)