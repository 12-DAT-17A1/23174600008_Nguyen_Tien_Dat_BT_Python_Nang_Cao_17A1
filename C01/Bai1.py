class Rectangle:
    danhsach = []
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def dien_tich(self):
        return self.length * self.width
    def chu_vi(self):
        return (self.length + self.width) * 2
    def show(self):
        print('Diện tích hình chữ nhật là:',self.dien_tich())
        print('Chu vi hình chữ nhật là:',self.chu_vi())
    @classmethod
    def main(cls):
        length = int(input('Nhập độ dài: '))
        width = int(input('Nhập chiều rộng: '))
        reg  =  cls(length,width)
        reg.show()
Rectangle.main()
        