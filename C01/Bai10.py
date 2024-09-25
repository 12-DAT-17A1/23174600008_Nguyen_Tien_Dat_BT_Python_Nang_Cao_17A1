from functools import reduce
from math import prod
from numpy import prod


class Diem:
    def __init__(self,x: int,y: int,so_do: list):
        self.x = x
        self.y = y
        self.so_do = so_do
    def tinh_dien_tich(self):
        return 3.14 * reduce(lambda x, y: x * y,self.so_do)
class Elip(Diem):
    def __init__(self,ban_kinh1,ban_kinh2,x,y):
        super().__init__(x,y,[ban_kinh1,ban_kinh2])
        self.ban_kinh1 = ban_kinh1
        self.ban_kinh2 = ban_kinh2
class DuongTron(Elip):
    def __init__(self,x,y,ban_kinh):
        super().__init__(ban_kinh,ban_kinh,x,y)
        self.ban_kinh = ban_kinh


def main():
    print('Hình Elip:')
    elip = Elip(4,8,2,2)
    print('Diện tích hình elip:',elip.tinh_dien_tich())
    print('Hình tròn:')
    ht = DuongTron(2,2,4)
    print('Diện tích hình tròn:',ht.tinh_dien_tich())
if __name__ == '__main__':
    main()
    