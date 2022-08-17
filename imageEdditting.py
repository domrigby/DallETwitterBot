from PIL import Image


class EditImage():

    def __init__(self,file):
        self.file = file
        self.img = Image.open(file)

    def crop(self):
        new_img = self.img.crop((450,0,1450,900))
        new_img.save(self.file)