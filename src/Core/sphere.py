from hittable import *

class Sphere(Hittable):
    def __init__(self, center : Point3, radius : float):
        super().__init__()
        self.center = center
        self.radius = radius

    def hit(self, r, ray_tmin, ray_tmax, hit_record):
        oc = self.center - r.origin
        a = r.direction.dot(r.direction)
        b = -2 * r.direction.dot(oc)
        c = oc.dot(oc) - self.radius**2
        delta = b**2 - 4*a*c

        if delta < 0:
            return False
        return True

