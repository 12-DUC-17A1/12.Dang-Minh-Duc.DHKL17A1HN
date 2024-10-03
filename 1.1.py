class hinhchunhat:
    def __init__(seft, chieu_dai=0, chieu_rong=0):
        seft.chieu_dai=chieu_dai
        seft.chieu_rong=chieu_rong
    def nhap_du_lieu(seft):
        seft.chieu_dai=float(input("moi nhap chieu dai:"))
        seft.chieu_rong=float(input("moi nhap chieu rong:"))
    def tinh_dien_tich(seft):
        return seft.chieu_dai*seft.chieu_rong
    def tinh_chu_vi(seft):
        return (seft.chieu_dai+seft.chieu_rong)*2
    def in_du_lieu(seft):
        print(f"chieu dai:{seft.chieu_dai}")
        print(f"chieu rong:{seft.chieu_rong}")
        print(f"dien tich:{seft.tinh_dien_tich()}")
        print(f"chu vi:{seft.tinh_chu_vi()}")
# chuong trinh chay
if __name__=="__main__":
    hcn=hinhchunhat()
    hcn.nhap_du_lieu()
    hcn.in_du_lieu()