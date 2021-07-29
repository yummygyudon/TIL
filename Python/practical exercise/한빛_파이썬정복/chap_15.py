#15단원 2번문제
#화소 수, 줌 배율을 속성으로 가지고 사진을 찍는 동작을 수행하는 Camera 클래스를 작성하라.

class Camera :
    def __init__(self, pixels, zoom):
        self.pixels = pixels
        self.zoom = zoom

    def getpictures(self):
        print(f"{self.pixels}화소의 카메라로 {self.zoom}배 줌으로 사진을 찍는다!")

samsung = Camera(1000000, 1.5)
samsung.getpictures()

