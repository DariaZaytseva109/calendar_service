# модель данных "Событие": ID, Дата, Заголовок, Текст
from datetime import datetime

class Event:
    def __init__(self, event_id: int, day: datetime, title: str, text: str):
        self.event_id = event_id
        self.day = day
        self.title = title
        self.text = text
