# xay dung mau phan so PS
class PS:
    def __init__(seft, tu_so=0, mau_so=1):
        seft.tu_so=tu_so
        # xay dung dieu kien
        if mau_so==0:
            print("mau so phai bang 1:")
            mau_so=1  
        else:
            seft.mau_so=mau_so
    def nhap(seft):
        seft.tu_so=int(input("moi nhap tu so:"))
        seft.mau_so=int(input("moi nhap mau so:"))
        while seft.mau_so==0:
            print("mau so phai bang 1:")
            seft.mau_so=int(input("moi nhap masu so:"))
    def in_du_lieu(seft):
        print(f"{seft.tu_so}//{seft.mau_so}")
# chay chuong trinh chinh
phan_so=PS()
phan_so.nhap()
phan_so.in_du_lieu()        