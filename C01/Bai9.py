#Lớp Đa Giác
class DaGiac:
    def __init__(self,so_canh:int,so_do_canh:list):
        self.so_canh = so_canh
        self.so_do_canh = so_do_canh
    def tinh_chu_vi(self):
        return sum(self.so_do_canh)
#Lớp hình bình hành kế thừa từ lớp da giác
class HinhBinhHanh(DaGiac):
    def __init__(self,canh_day,canh_ben,chieu_cao):
        super().__init__(4,[canh_day,canh_ben,canh_day,canh_ben])
        self.chieu_cao  = chieu_cao
        self.canh_ben = canh_ben
        self.canh_day  = canh_day
        
    def tinh_dien_tich(self):
        return self.canh_day * self.chieu_cao
#Lớp hình chữ nhật kế thừa từ lớp hình bình hành 
class HinhChuNhat(HinhBinhHanh):
    def __init__(self,chieu_dai, chieu_rong):
        super().__init__(chieu_dai,chieu_rong,chieu_rong)
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
#Lớp hình vuông kế thừa từ lớp hình chữ nhật.
class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh,canh)
        self.canh = canh
        
    def tinh_dien_tich(self):
        return self.canh ** 2
    
#Chương trình chính
def main():
    print('Hình bình hành:')
    hbh = HinhBinhHanh(5,3,4)
    print(f"Chu vi của hbh là: {hbh.tinh_chu_vi()}")
    print(f"Diện tích của hbh là: {hbh.tinh_dien_tich()}")
    
    print('\nHình chữ nhật:')
    hcn = HinhChuNhat(6,4)
    print(f"Chu vi của hcn là: {hcn.tinh_chu_vi()}")
    print(f"Diện tích của hcn là: {hcn.tinh_dien_tich()}")
    
    print('\nHình chữ nhật:')
    hv = HinhVuong(5)
    print(f"Chu vi của hv là: {hv.tinh_chu_vi()}")
    print(f"Diện tích của hv là: {hv.tinh_dien_tich()}")




if __name__ == '__main__':
    main()
        
