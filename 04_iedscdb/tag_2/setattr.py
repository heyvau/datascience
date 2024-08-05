"""
setattr (Schwer)
Wir haben eine Klasse LineItem gegeben. Erstelle LineItem-Objekte und speichere
sie in einer Liste line_items. Achte in __init__ darauf, dass die Werte in
**kwargs übergeben werden und erstelle dynamisch die Attribute.
Es muss __repr__ implementiert sein, __exakt__ wie unten gezeigt.
"""
from pprint import pprint


class LineItem:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


    def __repr__(self):
        return (
            f"<{self.__class__.__name__}(" + 
            ", ".join([f"{k}={v!r}" for k, v in self.__dict__.items()]) +
            ")>")


lines = [
    {
        "id": 3,
        "name": "Pencil Geha",
        "style": "bold",
        "color": "black",
    },
    {
        "id": 13,
        "name": "Pencil Geha Professional",
        "style": "bold",
        "color": "red",
    },
    {
        "id": 23,
        "name": "Parker Chef",
        "style": "thin",
        "color": "silver",
        "bevel": True,
    },
]

line_items = [LineItem(**line) for line in lines]
pprint(line_items)
# Result:
# [
# <LineItem(id=3, name='Pencil Geha', style='bold', color='black')>,
# <LineItem(id=13, name='Pencil Geha Professional', style='bold', color='red')>,
# <LineItem(id=23, name='Parker Chef', style='thin', color='silver', bevel=True)>
# ]
