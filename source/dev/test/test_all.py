import pytest

import classes

import g_saver

from SmartCity import SmartCity
from TrafficSystem.Car import Car
from SystemSaver import SystemSaver
from classes.Service.TrafficManager import TrafficManager

def test_g_saver(monkeypatch):
    assert g_saver is not None

    save_data = []

    def mock_save(self):
        for serializable in self._SystemSaver__serializables:
            save_data.append(serializable)

    monkeypatch.setattr(classes.g_saver, 'save', mock_save)
    Car()
    classes.g_saver.save(classes.g_saver)

    assert len(save_data) > 0


def test_CityCreation():
    smartcity = SmartCity()
    assert len(smartcity.c_sensors) > 0 # Check is all sensors are created correctly
    assert 'GasSensor' in smartcity.sensors.keys()
