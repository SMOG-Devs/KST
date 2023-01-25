from typing import List
import backend.kst_app.data_storage.models as m


def mine_ids_sorted() -> List[int]:
    sensors = m.get_all_sensors()
    sensors = sorted(sensors, key=lambda sensor: sensor.id)
    return [sensor.id for sensor in sensors]
