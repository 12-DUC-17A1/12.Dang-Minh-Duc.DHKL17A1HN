# xay dung lop diem
import math
class diem:
    def __init__(seft, x=0, y=0):
        seft.x=x
        seft.y=y
    def display(seft):
        print(f"hien thi toa do:{seft.x},{seft.y}")
class elip(diem):
    def __init__(seft,x=0, y=0, a=1, b=1):
        super().__init__(x,y)
        seft.a=a# ba truc toa do lon        
        seft.b=b# ban truc toa do nho
    def dien_tich(seft):
        return math.pi*seft.a*seft.b
    def display(seft):
        super().display()
        print(f"truc toa do cua a va b:{seft.a}, {seft.b}")
        print(f"dien tich hinh elip la:{seft.dien_tich()}")
class duong_tron(elip):
    def __init__(seft, x=0, y=0, r=1):# a=b bang r
        super().__init__(x,y,r)
        seft.r=r
    def dien_tich_dtron(seft):
        return math.pi*seft.r**seft.r
    def display(seft):
        super().display()
        print(f"ban kinh duong tron:{seft.r}")
        print(f"dien tich duong tron:{seft.display}")
# chay chuong trinh
def main():
    ELIP=elip(2,4,5,6)
    print()
    ELIP.display()
    print()
    DT=duong_tron(3,4,5)
    print()
    DT.display()
    print()
if __name__=="__main__":
    main()
