class Image:

    def __init__(self, path):
        self.path = path

    def display(self):
        pass


class RealImage(Image):

    def __init__(self, path):
        super().__init__(path)
        self.raw_data = None
        self.load_from_disk()

    def load_from_disk(self):
        print('load image from disk')
        self.raw_data = 'rgb data'

    def display(self):
        print('display image')


class ImageProxy(Image):

    def __init__(self, path):
        super().__init__(path)
        self._image = None

    def display(self):
        if self._image is None:
            self._image = RealImage(self.path)
        self._image.display()


if __name__ == '__main__':
    image = ImageProxy('./demo.png')  # image is not loaded
    print(image._image)
    image.display()  # image is loaded
    print(image._image)
    image.display()
