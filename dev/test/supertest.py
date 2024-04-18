import pytest

from classes.SmartCity import SmartCity
from classes.TrafficSystem.Car import Car

import classes
import classes.globals


def test_g_saver(monkeypatch):
    assert classes.g_saver is not None

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
    assert 'GasSensor' in smartcity.sensors


@pytest.mark.parametrize('name', ['Renault', 'Nissan'])
def test_entityCreation(name):
    smartCity = SmartCity()
    car = Car(name=name)
    smartCity.transport.append(car)

    assert car.name == name
    assert car.id in classes.globals.g_trafficObjectPool
    assert car in smartCity.transport
