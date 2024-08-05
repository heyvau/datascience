""" (MITTEL)
Erstelle eine Klasse CSV-Manager, die eine CSV-Datei einliest. 
Die ausgegeben Felder sollen über eine Property columns gesetzt werden können.
Implementiere die read()-Methode als Generator-Funktion

Beispiel:
manager = CsvManager(filename="data.csv")
manager.columns = ["id", "age", "height"]
data = manager.read()

print(data)
{'id': '23', 'age': '4', 'height': '2'}
{'id': '223', 'age': '14', 'height': '22'}
{'id': '123', 'age': '4', 'height': '3422'}
"""

from pathlib import Path
import csv
from typing import List, Dict, Generator


BASE_DIR = Path(__file__).resolve().parent


class CsvManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.columns = []


    @property
    def filename(self):
        return self._filename
    

    @filename.setter
    def filename(self, filename: str):
        if not isinstance(filename, str):
            raise TypeError("argument: str")
        
        self._filename = BASE_DIR / filename
        print(self._filename)
        
    
    @property
    def columns(self):
        return self._columns
    

    @columns.setter
    def columns(self, columns: List[str]):
        if not (
            isinstance(columns, List)
            and 
            all([isinstance(col, str) for col in columns])
        ):
            raise TypeError("argument: List[str]")
        self._columns = columns
            

    def read_data(self) -> Generator:
        if not self.filename.is_file():
            raise FileNotFoundError("File for reading wasn't found.")
        
        with open(self.filename) as file:
            csv_reader = csv.DictReader(file)
            yield from csv_reader

            # for row in csv_reader:
            #     yield {col: row[col] for col in self.columns}


    def write_data(self, data_to_write: List[Dict]) -> None:
        if not (
            isinstance(data_to_write, List)
            and 
            all([isinstance(line, Dict) for line in data_to_write])
        ):
            raise TypeError("argument: List[Dict]")
        
        with open(self.filename, "w") as file:
            csv_writer = csv.DictWriter(file, fieldnames=self.columns)

            csv_writer.writeheader()
            csv_writer.writerows(data_to_write)
        
    
    def print_data(self, data: Generator) -> None:
        for line in data:
            print(line)


if __name__ == "__main__":

    data_to_write = [
        {'id': '23', 'age': '4', 'height': '2'},
        {'id': '223', 'age': '14', 'height': '22'},
        {'id': '123', 'age': '4', 'height': '3422'}
    ]
    
    manager = CsvManager(filename="data.csv")
    manager.columns = ["id", "height"]
    # manager.write_data(data_to_write=data_to_write)
    data_gen = manager.read_data()
    manager.print_data(data=data_gen)
