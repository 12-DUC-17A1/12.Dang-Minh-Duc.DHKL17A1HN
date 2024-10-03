import math

class TamGiac:
    def __init__(self, a, b, c):
        """Khởi tạo tam giác với 3 cạnh a, b, c"""
        self.a = a
        self.b = b
        self.c = c

    def la_tam_giac_hop_le(self):
        """Kiểm tra tam giác có hợp lệ không"""
        return (self.a + self.b > self.c and 
                self.a + self.c > self.b and 
                self.b + self.c > self.a)

    def chu_vi(self):
        """Tính chu vi tam giác"""
        if self.la_tam_giac_hop_le():
            return self.a + self.b + self.c
        else:
            return "Không phải tam giác hợp lệ"

    def dien_tich(self):
        """Tính diện tích tam giác bằng công thức Heron"""
        if self.la_tam_giac_hop_le():
            p = self.chu_vi() / 2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        else:
            return "Không thể tính diện tích cho tam giác không hợp lệ"
class TamGiacCan(TamGiac):
    def __init__(self, a, c):
        """Khởi tạo tam giác cân với hai cạnh a và cạnh đáy c"""
        super().__init__(a, a, c)  # Hai cạnh a bằng nhau, cạnh c là đáy

    def dien_tich(self):
        """Tính diện tích tam giác cân"""
        if self.la_tam_giac_hop_le():
            # Tính chiều cao của tam giác cân
            h = math.sqrt(self.a ** 2 - (self.c / 2) ** 2)
            return 0.5 * self.c * h
        else:
            return "Không thể tính diện tích cho tam giác không hợp lệ"
class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        """Khởi tạo tam giác vuông với 2 cạnh góc vuông a và b, cạnh huyền tính theo định lý Pythagoras"""
        c = math.sqrt(a ** 2 + b ** 2)  # Cạnh huyền
        super().__init__(a, b, c)

    def dien_tich(self):
        """Tính diện tích tam giác vuông"""
        return 0.5 * self.a * self.b  # Diện tích tam giác vuông = 1/2 tích của 2 cạnh góc vuông
class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        """Khởi tạo tam giác đều với 3 cạnh bằng nhau"""
        super().__init__(a, a)  # Tam giác đều là tam giác cân có 3 cạnh bằng nhau

    def dien_tich(self):
        """Tính diện tích tam giác đều"""
        return (math.sqrt(3) / 4) * self.a ** 2  # Diện tích tam giác đều = (sqrt(3) / 4) * a^2
# Tam giác thường
tam_giac = TamGiac(3, 4, 5)
print("Chu vi tam giác:", tam_giac.chu_vi())
print("Diện tích tam giác:", tam_giac.dien_tich())

# Tam giác cân
tam_giac_can = TamGiacCan(5, 6)
print("Chu vi tam giác cân:", tam_giac_can.chu_vi())
print("Diện tích tam giác cân:", tam_giac_can.dien_tich())

# Tam giác vuông
tam_giac_vuong = TamGiacVuong(3, 4)
print("Chu vi tam giác vuông:", tam_giac_vuong.chu_vi())
print("Diện tích tam giác vuông:", tam_giac_vuong.dien_tich())

# Tam giác đều
tam_giac_deu = TamGiacDeu(4)
print("Chu vi tam giác đều:", tam_giac_deu.chu_vi())
print("Diện tích tam giác đều:", tam_giac_deu.dien_tich())
