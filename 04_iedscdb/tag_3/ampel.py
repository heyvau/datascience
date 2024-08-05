"""
Eine Ampel kann immer nur den Zustand rot, gelb oder grün annehmen.

Definiere einen StrEnum TrafficLightState, der die Zustände einer
Ampel repräsentiert: ROT, GELB, und GRÜN.

Erstelle eine TrafficLight-Klasse, deren Anfangszustand ROT ist.

Die next_state-Methode simuliert den Übergang von einem
Zustand zum nächsten in der Reihenfolge ROT → GRÜN → GELB → ROT...

Simulieren die Zustandsübergänge durch wiederholte Aufrufe von next_state().

traffic_light = TrafficLight()
print("Initial state:", traffic_light) # rot
traffic_light.next_state()
print("Current state:", traffic_light) # grün

for _ in range(5):
    traffic_light.next_state()
    print("Next state:", traffic_light)

Next state: yellow
Next state: red
Next state: green
Next state: yellow
Next state: red

"""

from enum import StrEnum


class TrafficLightState(StrEnum):
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"


class TrafficLight:
    def __init__(self):
        self.state  = TrafficLightState.RED


    def __repr__(self) -> str:
        return f"{self.state}"


    def next_state(self):
        match self.state:

            case TrafficLightState.RED:
                self.state  = TrafficLightState.GREEN

            case TrafficLightState.GREEN:
                self.state  = TrafficLightState.YELLOW

            case TrafficLightState.YELLOW:
                self.state  = TrafficLightState.RED


if __name__ == "__main__":

    traffic_light = TrafficLight()
    print("Initial state:", traffic_light)

    traffic_light.next_state()
    print("Current state:", traffic_light)

    for _ in range(5):
        traffic_light.next_state()
        print("Next state:", traffic_light)
