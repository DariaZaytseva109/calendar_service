from flask import Flask, request
from datetime import datetime

import model

app = Flask(__name__)


API_ROOT = '/api/v1'
EVENT_API_ROOT = API_ROOT + '/event'


class API_exeption(Exception):
    pass


def from_raw_to_event(raw_event: str) -> model.Event:   #форматирование из строки (self, id: int, day: datetime, title: str, text: str):
    try:
        event_list_data = raw_event.split('|')
        event_id = int(event_list_data[0].replace('-', ''))
        day = datetime.strptime(event_list_data[0], '%Y-%m-%d')
        title = event_list_data[1]
        text = event_list_data[2]
        event = model.Event(event_id, day, title, text)

        return event
    except Exception:
        raise API_exeption('Неверный формат ввода данных')


def to_raw(event: model.Event) -> str:
    return f'{event.day.strftime("%Y-%m-%d")}|{event.title}|{event.text}'


@app.route(EVENT_API_ROOT + '/', methods=['POST'])
def create():
    data = request.get_data().decode('utf-8')
    event = from_raw_to_event(data)
    return f'Создано новое событие: {event.title}. Дата: {event.day.strftime("%Y-%m-%d")}'



@app.route(EVENT_API_ROOT + '/', methods=['GET'])
def list():
    return 'list'



@app.route(EVENT_API_ROOT + '/<id>/', methods=['GET'])
def read(id):
    return 'read'


@app.route(EVENT_API_ROOT + '/<id>/', methods=['PUT'])
def update(id):
    return 'update'



@app.route(EVENT_API_ROOT + '/<id>/', methods=['DELETE'])
def delete(id):
    return 'delete'



if __name__ == '__main__':
    app.run(debug=True)