from classes.SmartCity import SmartCity
from classes.TrafficSystem.Car import Car
import classes


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


def test_CityCreation(monkeypatch):
    smartcity = SmartCity()
    assert len(smartcity.c_sensors) > 0 # Check is all sensors are created correctly

