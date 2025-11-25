from ray import *
from Math.vector import *

class HitRecord:
    point : Point3
    normal : Vector3
    distance : float


class Hittable:
    def __init__(self):
        pass

    def hit(self, r : Ray, ray_tmin : float, ray_tmax : float, hit_record : HitRecord) -> bool:
        pass