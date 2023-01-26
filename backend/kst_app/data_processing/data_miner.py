from typing import List
from kst_app.data_storage.models import get_all_sensors


def mine_ids_sorted() -> List[int]:
    sensors = get_all_sensors()
    sensors = sorted(sensors, key=lambda sensor: sensor.id)
    return [sensor.id for sensor in sensors]
