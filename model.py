# модель данных "Событие": ID, Дата, Заголовок, Текст
from datetime import datetime, date

class Event:
    def __init__(self, id: int, day: datetime, title: str, text: str):
        self.id = id
        self.day = day
        self.title = title
        self.text = text