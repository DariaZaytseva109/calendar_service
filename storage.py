import model
from datetime import datetime



class Storage_Exception(Exception):
    pass

class Local_Storage:
    def __init__(self):
        self.storage = {}

    def create(self, event: model.Event):
        try:
            self.storage[event.day] = event
        except Exception:
            raise Storage_Exception('Failed to create an event')

    def list(self):
        try:
            return self.storage.values()
        except Exception:
            raise Storage_Exception('Failed to store an event')

    def read(self, day: str):     #дата в формате ГГГГ-ММ-ДД
        try:
            return self.storage[datetime.strptime(day, "%Y-%m-%d")]
        except Exception:
            raise Storage_Exception('Event not found')

    def update(self, day: str, event: model.Event):
        try:
            self.storage[datetime.strptime(day, "%Y-%m-%d")] = event
        except Exception:
            raise Storage_Exception('Failed to update')

    def delete(self, day: str):
        try:
            del self.storage[datetime.strptime(day, "%Y-%m-%d")]
        except Exception:
            raise Storage_Exception('Failed to delete')