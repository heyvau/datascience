import pymongo
from pymongo.collection import Collection
from world_cities import city, cities


def insert_city(cities: Collection, city_data: dict) -> None:
    cities.insert_one(city_data)


def insert_cities(cities: Collection, cities_data: list[dict]) -> None:
    cities.insert_many(cities_data)


def show_cities(
    cities: Collection,
    search_criteria: dict = {},
    sort_criteria: str = "name",
    sort_direction: int = 1
    ) -> None:
    
        city_entries = db.cities.find(search_criteria).sort(sort_criteria, sort_direction)
        for entry in city_entries:
            for k, v in entry.items():
                print(f"{k}: {v}")
            print("--------------------")

def show_million_cities(cities: Collection):
    show_cities(cities, search_criteria={"population": {"$gt": 1000000}})


def show_city_by_name(cities: Collection, city_name: str):
    show_cities(cities, search_criteria={"name": city_name})


def show_cities_by_country(cities: Collection, country_name: str):
    show_cities(cities, search_criteria={"country": country_name})


def show_cities_sorted_by_population(cities: Collection):
    show_cities(cities, sort_criteria="population")


def show_cities_sorted_by_area(cities: Collection):
    show_cities(cities, sort_criteria="area")


if __name__ == "__main__":
    with pymongo.MongoClient("mongodb://localhost:27017") as client:
        db = client.WorldCitiesDB

        # insert_city(db.cities, city)

        # insert_cities(db.cities, cities)
        
        # print("Alle Städte", end="\n\n")
        # # show_cities(db.cities)

        # print("Städte mit Bevölkerung > 1000000", end="\n\n")
        # # show_million_cities(db.cities)

        # print("Suche nach einer spezifischen Stadt anhand ihres Namens", end="\n\n")
        # show_city_by_name(db.cities, "Osaka")

        # print("Städte in einem bestimmten Land", end="\n\n")
        # show_cities_by_country(db.cities, "Germany")

        show_cities_sorted_by_population(db.cities)
