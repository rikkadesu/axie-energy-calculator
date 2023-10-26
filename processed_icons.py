from PIL import Image, ImageTk


class Icons:
    def __init__(self):
        self.bloodmoon_icon = None

    @staticmethod
    def get_bloodmoon_icon_30x30(self):
        bloodmoon_image = Image.open("icons/bloodmoon.png")
        width, height = 30, 30
        bloodmoon_image_resized = bloodmoon_image.resize((width, height))
        self.bloodmoon_icon = ImageTk.PhotoImage(bloodmoon_image_resized)
        return self.bloodmoon_icon