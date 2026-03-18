import io
import json

from rest_framework.parsers import JSONParser

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data, separators=(",", ":")).encode()


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    parsed = JSONParser().parse(stream)
    serializer = CarSerializer(data=parsed)
    serializer.is_valid(raise_exception=True)
    return Car(**serializer.validated_data, id=parsed.get("id"))
