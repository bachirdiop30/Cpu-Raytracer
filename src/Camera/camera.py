from Math.vector import Point3, Vector3, Color3
from Core.primitives import hit_sphere
from Core.ray import Ray
from Display.PPMWriter import PPMWriter

class Camera:
    def __init__(self, img_width, aspect_ratio) -> None:
        self._img_width = img_width
        self._aspect_ratio = aspect_ratio
        self._img_height = 0
        self._center = None
        self._pixel00_loc = None
        self._pixel_delta_u = None
        self._pixel_delta_v = None
        self._img_ro_render = []

    def ray_color(self, ray):
        t = hit_sphere(Vector3(0,0,-1), 0.5, ray)
        if t:
            N = (ray.at(t) - Vector3(0,0,-1)).normalize()
            return 0.5 * Color3(N.x + 1, N.y + 1, N.z + 1)

        unit_dir = ray.direction.normalize()
        a = 0.5 * (unit_dir.y + 1.0)
        return (1.0 - a) * Color3(1,1,1) + a * Color3(0.5, 0.7, 1.0)

    def initialize_camera(self):
        self._img_height = int(self._img_width / self._aspect_ratio)
        self._center = Point3(0, 0, 0)

        #focal_length = 1.0
        viewport_height = 2.0
        viewport_width = viewport_height * (self._img_width / self._img_height)

        viewport_u = Vector3(viewport_width, 0, 0)
        viewport_v = Vector3(0, -viewport_height, 0)

        self._pixel_delta_u = viewport_u / self._img_width
        self._pixel_delta_v = viewport_v / self._img_height

        viewport_upper_left = self._center - Vector3(0, 0, 1) - viewport_u/2 - viewport_v/2
        self._pixel00_loc = viewport_upper_left + 0.5 * (self._pixel_delta_u + self._pixel_delta_v)

    def write_img_to_file(self):
        with open("output.ppm", "w") as f:
            writer = PPMWriter(self._img_width, self._img_height, f)
            writer.write_image(self._img_ro_render)


    def render(self):
        #TODO: add hittables abstraction layer to primitives
        self.initialize_camera()
        
        for j in range(self._img_height):
            row = []
            for i in range(self._img_width):
                pixel_center = self._pixel00_loc + (i+0.5)*self._pixel_delta_u + (j+0.5)*self._pixel_delta_v
                ray_direction = pixel_center - self._center
                r = Ray(self._center, ray_direction)
                row.append(self.ray_color(r))
            self._img_ro_render.append(row)

        self.write_img_to_file()


