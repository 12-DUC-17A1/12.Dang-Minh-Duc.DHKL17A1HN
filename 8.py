#xay dung ngay, thang, nam
class date:
    def __init__(seft, day=1, month=1, year=1969):
        seft.day=day
        seft.month=month
        seft.year=year
     # Ghi đè phương thức __str__ để định nghĩa cách hiển thị Date khi in ra
    def __str__(self):
        return f"{self.day:02}/{self.month:02}/{self.year}"
    def display(seft):
        print(seft)
    def next(seft):
        day_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
        # kiem tra nam nhuan
        if(seft.day%4==0 and seft.day%100!=0) or (seft.day%400==0):
            day_in_month[1]=29# kiem tra thang 2 co 29 ngay khong
        # tinh ngay
        seft.day+=1
        if seft.day>day_in_month[seft.month-1]:
            seft.day=1
            seft.month+=1
            if seft.month>12:
                seft.month=1
                seft.year+=1
class employee:
    def __init__(seft, ten, ngay_sinh, ngay_vao_cong_ty):
        seft.ten=ten
        seft.ngay_sinh=ngay_sinh
        seft.ngay_vao_cong_ty=ngay_vao_cong_ty
    def display(seft):
        print(f"ho ten:{seft.ten}, ngay sinh:{seft.ngay_sinh},ngay vao cong ty:{seft.ngay_vao_cong_ty}")
# chay chuong trinh chinh
ngay_sinh=date(3,4,2005)
ngay_vao_cong_ty=date(3,4,1999)
# xay dung nhan vien
EMPLOYEE=employee("DANG MINH DUC",ngay_sinh,ngay_vao_cong_ty)
# chay
EMPLOYEE.display()