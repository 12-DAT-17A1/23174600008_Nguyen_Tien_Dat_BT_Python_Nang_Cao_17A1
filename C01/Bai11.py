class TamGiac:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def tinh_chu_vi(self):
        return self.a + self.b + self.c
    
class  TamGiacVuong(TamGiac):
    def __init__(self,a,b,canh_huyen):
        super().__init__(a,b,canh_huyen)
    def tinh_dien_tich(self):
        return (1/2) * self.a * self.b

class TamGiacCan(TamGiac):
    def __init__(self, canh_ben,canh_day):
        super().__init__(canh_ben, canh_ben, canh_day)
        self.canh_ben = canh_ben
        self.canh_day = canh_day
        
    def tinh_dien_tich(self):
        p = (self.canh_ben + self.b + self.c) / 2
        return (p * (p - self.canh_ben) * (p - self.canh_ben) * (p - self.canh_day)) ** 0.5
    
class TamGiacDeu(TamGiac):
    def __init__(self,a):
        super().__init__(a,a,a)
    
    def tinh_dien_tich(self):
        return (3 ** 0.5 / 4) * self.a ** 2
    
    
def main():
    print('Tam giác vuông:')
    tgv = TamGiacVuong(4,5,6)
    print(f'Chu vi tam giác vuông là: {tgv.tinh_chu_vi()}')
    print(f'Diện tích tam giác vuông là: {tgv.tinh_dien_tich()}')
    print('\nTam giác cân:')
    tgc = TamGiacCan(4,5)
    print(f'Chu vi tam giác cân là: {tgc.tinh_chu_vi()}')
    print(f'Diện tích tam giác cân là: {tgc.tinh_dien_tich()}')
    print('\nTam giác đều:')
    tgd = TamGiacDeu(4)
    print(f'Chu vi tam giác đều là: {tgd.tinh_chu_vi()}')
    print(f'Diện tích tam giác đều là: {tgd.tinh_dien_tich()}')







if __name__ == '__main__':
    main()