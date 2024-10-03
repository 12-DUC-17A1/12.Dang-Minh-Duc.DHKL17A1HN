class da_giac:
    def __init__(seft, so_canh_da_giac):
        seft.so_canh_da_giac=so_canh_da_giac
class hinh_binh_hanh(da_giac):
    def __init__(seft,day, canh_ben, chieu_cao):
        super().__init__(4)# hinh binh hanh co 4 canh
        seft.day=day
        seft.canh_ben=canh_ben
        seft.chieu_Cao=chieu_cao
    # tinh chu vi hinh binh hanh
    def chu_vi_hinh_binh_hanh(seft):
        return 2*(seft.day+seft.canh_ben)
    # tinh den tich hinh binh hanh
    def dien_tich_hinh_binh_hanh(seft):
        return seft.day*seft.chieu_Cao
class hinh_chu_nhat(hinh_binh_hanh):
    def __init__(seft, chieu_dai, chieu_rong):
        super().__init__(chieu_dai,chieu_rong,chieu_rong)
        seft.chieu_dai=chieu_dai
        seft.chieu_rong=chieu_rong
    # tinh dien tich hinh chu nhat
    def dien_tich_hcn(seft):
        return seft.chieu_dai*seft.chieu_rong
    # tinh chu vi hinh chu nhat
    def chu_vi_hcn(seft):
        return 2*(seft.chieu_dai+seft.chieu_rong)
class hinh_vuong(hinh_chu_nhat):
    def __init__(seft, canh):
        super().__init__(seft, canh)
        seft.canh=canh
    # tinh chhu vi hinh vuong
    def chu_vi_hv(seft):
        return seft.canh**2
    # dien tinh hinh vuong
    def dt_hv(seft):
        return 4*seft.canh
def main():
    # nhap thong tin cho hbh
    print("thong tin hinh binh hanh:")
    day=float(input("moi nhasp day:"))
    canh_ben=float(input("moi nhap canh ben:"))
    chieu_cao=float(input("moi nhap chieu cao"))
    HBH=hinh_binh_hanh(day,canh_ben,chieu_cao)
    print(f"cv hinh binh hanh:{HBH.chu_vi_hinh_binh_hanh()}")
    print(f"dien tich hinh binh hanh:{HBH.dien_tich_hinh_binh_hanh()}")
    # nhap thong tin cho hcn
    print("moi nhap thong tin hinh chu nhat")
    chieu_dai=float(input("moi nhap chieu dai:"))
    chieu_rong=float(input("moi nhap chieu rong:"))
    HCN=hinh_chu_nhat(chieu_dai,chieu_rong)
    print(f"dien tich hinh chu nhat;{HCN.dien_tich_hcn()}")
    print(f"chu vi hinh chu nhat:{HCN.chu_vi_hcn()}")
    # nhap thong tin cho hv
    print("moi nhap thong tin hinh vuong")
    canh=float(input("moi nhap chieu canh:"))
    HV=hinh_vuong(canh)
    print(f"dien tich hv:{HV.dt_hv()}")
    print(f"chu vi hinh vuong:{HV.chu_vi_hv()}")
if __name__=="__main__":
    main()

