class PS:
    def __init__(self,tu_so,mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.kiem_tra_tinh_hop_le()
    def kiem_tra_tinh_hop_le(self):
        return isinstance(self.tu_so,int) and isinstance(self.mau_so,int) and self.mau_so != 0
    def in_phan_so(self):
        print('Phân số: %d / %d'%(self.tu_so,self.mau_so))
    @classmethod
    def main(cls):
        while True:
            try:
                tu_so = int(input('Nhập tử số: '))
                mau_so = int(input('Nhập mẫu số: '))
                break
            except ValueError:
                print('Lỗi sai kiểu dữ liệu nhập, phải là kiểu số nguyên')
        phan_so = cls(tu_so,mau_so)
        if phan_so.kiem_tra_tinh_hop_le():
            phan_so.in_phan_so()
        else:
            print('Đây không phải là phân số')
            
            
PS.main()