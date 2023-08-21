import model
from datetime import datetime



class Storage_Exception(Exception):
    pass

class Local_Storage:
    def __init__(self):
        self.storage = {}

    def create(self, event: model.Event):
        try:
            self.storage[event.event_id] = event
        except Exception:
            raise Storage_Exception('Failed to create an event')

    def list(self):
        try:
            return self.storage.values()
        except Exception:
            raise Storage_Exception('Failed list events')

    def read(self, event_id: str):
        try:
            return self.storage[event_id]
        except Exception:
            raise Storage_Exception('Event not found')

    def update(self, event_id: str, event: model.Event):
        try:
            self.storage[event_id] = event
        except Exception:
            raise Storage_Exception('Failed to update')

    def delete(self, event_id: str):
        try:
            del self.storage[event_id]
        except Exception:
            raise Storage_Exception('Failed to delete')