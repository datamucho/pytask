import pygame

# initialize pygame and screen
pygame.init()
screen = pygame.display.set_mode((1200, 400))

# load the image and convert to numpy array
        
class GrayScaleTransformer():
    def __init__(self, image_file):
        self.image_file = image_file
        self.img = None
        self.arr = None
    
    def load_image(self):
        self.img = pygame.image.load(self.image_file).convert_alpha()
        self.arr = pygame.surfarray.array3d(self.img)
        print(self.arr.shape)
    
    def transform(self):
        for i in range(self.arr.shape[0]):
            for j in range(self.arr.shape[1]):
                r, g, b = self.arr[i][j]
                avg = r/3  + g/3  + b/3
                self.arr[i][j] = [avg, avg, avg]
    def save_image(self, image_file):
        surface = pygame.surfarray.make_surface(self.arr)
        pygame.image.save(surface, image_file) 

image_file = "data/test_cut.png"
transformer = GrayScaleTransformer(image_file)

transformer.load_image()
transformer.transform()
transformer.save_image("data/test_gray.png")


