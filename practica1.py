import json
from extras.utils import singleton
from websocket import create_connection

class RequestWs:
    def __init__(self):
        self.__elements = []

    def connect_ws(self):
        return create_connection("ws://209.126.82.146:8080")

    def request(self):
        self.ws = self.connect_ws()
        self.__elements.clear()
        while len(self.__elements) < 60000:
            self.__elements.append(json.loads(self.ws.recv()))
        self.ws.close()
        return self.__elements

@singleton
class DataManager(RequestWs):        
    def data_validation(self, elements):
        self.__data = {
            'max_num': 0,
            'min_num': 9999999999,
            'even_numbers': 0,
            'odd_numbers': 0,
            'prime_numbers': 0,
            'first_number': elements[0]['b'],
            'last_number': elements[-1]['b']
        }
        for element in elements:
            if element['b'] > self.__data.get('max_num'): self.__data['max_num'] = element['b']
            if element['b'] < self.__data.get('min_num'): self.__data['min_num'] = element['b']
            if element['b']%2 == 0: self.__data['even_numbers'] += 1
            if element['b']%2 != 0: self.__data['odd_numbers'] += 1
            if element['b']%2!=0 and element['b']%3!=0 and element['b']%5!=0 and element['b']%7!=0:
                self.__data['prime_numbers'] += 1
        
        return self.__data

    def loop(self):
        elements = self.request()
        return self.get_data(elements)

    def get_data(self, elements):
        data = self.data_validation(elements)
        print(data)
        return self.loop()