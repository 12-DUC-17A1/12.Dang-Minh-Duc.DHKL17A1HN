# xay dung lop TS
class TS:
    def __init__(seft, ho_ten="", diem_toan=0, diem_ly=0, diem_hoa=0):
        seft.ho_ten=ho_ten
        seft.diem_toan=diem_toan
        seft.diem_ly=diem_ly
        seft.diem_hoa=diem_hoa
    def nhap_thong_tin_TS(seft):## nhap ttTS
        seft.ho_ten=input("moi nhap ten thi sinh:")
        seft.diem_toan=float(input("moi nhap so diem toan:"))
        seft.diem_ly=float(input("moi nhap diem ly:"))
        seft.diem_hoa=float(input("moi nhap diem hoa:"))
    def tong_diem(seft):
        return seft.diem_toan+seft.diem_ly+seft.diem_hoa
    def in_thong_tin(seft):
        print(f"ho ten thi sinh:{seft.ho_ten}")
        print(f"tong diem:{seft.tong_diem()}")
#chay chuong trinh
if __name__=="__main__":
    danh_sach_ts=[]
    so_luong=int(input("moi nhap so luong thi sinh:"))
# nhap thong tin thi sinh
    for i in range(so_luong):
        ts=TS()
        ts.nhap_thong_tin_TS()
        danh_sach_ts.append(ts)
# diem chuan >=20
    diem_chuan=20
    ds_trung_tuyen=[ts for ts in danh_sach_ts if ts.tong_diem()>=diem_chuan]
# sap xep ds theo thu tu giam dan
    ds_trung_tuyen.sort(key=lambda ts: ts.tong_diem, reverse=True)
    print("\danh sach trung tuyen")
    for ts in ds_trung_tuyen:
        ts.in_thong_tin()





