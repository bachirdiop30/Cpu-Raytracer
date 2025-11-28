from Camera.camera import *
from Primitives.primitives import *

import time

SAMPLES_PER_PIXEL = 300

def main():

    world = HittableList()
    world.add(Sphere(Point3(0,-100.5,-3), 100))
    # world.add(Sphere(Point3(0.0,0,-1.0), 0.5))
    world.add(Sphere(Point3(1.5,0,-2.0), 0.5))
    world.add(Sphere(Point3(-1.5,0,-2.0), 0.5))
    world.add(Plane(Point3(-2, -.8, -4), Vector3(1.5 * 3, 0, 0), Vector3(0, 1 * 3, 0)))

    camera = Camera(720, (16.0 / 9.0), samples_per_pixel=SAMPLES_PER_PIXEL, max_ray_bounces=50) # you guys can change the last variable for sampling rate, 5 is already high in python
    camera.render(world, output = "Results/Sortie.ppm")

if __name__ == "__main__":
    start = time.time()
    main()
    print(f"Took {time.time() - start}s")