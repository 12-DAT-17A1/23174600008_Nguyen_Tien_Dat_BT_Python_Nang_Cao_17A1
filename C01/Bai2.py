# Định nghĩa lớp TS (thí sinh)
class ThiSinh:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa
        self.tong_diem = self.tinh_tong_diem()

    # Hàm tính tổng điểm của thí sinh
    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    # Hàm in thông tin thí sinh
    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}, Toán: {self.diem_toan}, Lý: {self.diem_ly}, Hóa: {self.diem_hoa}, Tổng điểm: {self.tong_diem}")

# Hàm nhập thông tin danh sách thí sinh
def nhap_danh_sach_thi_sinh():
    danh_sach = []
    so_luong = int(input("Nhập số lượng thí sinh: "))
    for i in range(so_luong):
        ho_ten = input("Nhập họ tên thí sinh: ")
        diem_toan = float(input("Nhập điểm Toán: "))
        diem_ly = float(input("Nhập điểm Lý: "))
        diem_hoa = float(input("Nhập điểm Hóa: "))
        ts = ThiSinh(ho_ten, diem_toan, diem_ly, diem_hoa)
        danh_sach.append(ts)
    return danh_sach

# Hàm hiển thị danh sách thí sinh trúng tuyển (điểm chuẩn là 20)
def hien_thi_danh_sach_trung_tuyen(danh_sach, diem_chuan=20):
    danh_sach_trung_tuyen = [ts for ts in danh_sach if ts.tong_diem >= diem_chuan]
    danh_sach_trung_tuyen.sort(key=lambda ts: ts.tong_diem, reverse=True)

    print("\nDanh sách thí sinh trúng tuyển:")
    for ts in danh_sach_trung_tuyen:
        ts.in_thong_tin()

# Chương trình chính
if __name__ == "__main__":
    danh_sach_thi_sinh = nhap_danh_sach_thi_sinh()
    hien_thi_danh_sach_trung_tuyen(danh_sach_thi_sinh)
