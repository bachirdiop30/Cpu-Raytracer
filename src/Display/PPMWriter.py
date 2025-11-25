import io

def _clamp(x):
    return max(0.0, min(x, 1.0))

class PPMWriter:
    def __init__(self, width : int, height : int, output_stream : io.TextIOBase):
        self.width = width
        self.height = height
        self.output : io.TextIOBase = output_stream
        self._write_header()


    def _write_header(self):
        # P3
        self.output.write("P3\n")
        # width et height
        self.output.write(f"{self.width} {self.height}\n")
        # valeur rgb max
        self.output.write("255\n")

    def write_image(self, image):
        for row in image:
            # pixel : Vector3
            for pixel in row:
                r = _clamp(pixel.x)
                g = _clamp(pixel.y)
                b = _clamp(pixel.z)
                ir = int(255.999 * r)
                ig = int(255.999 * g)
                ib = int(255.999 * b)

                self.output.write(f"{ir} {ig} {ib} ")
            self.output.write("\n")


        