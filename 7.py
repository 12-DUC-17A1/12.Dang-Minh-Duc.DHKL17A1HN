# xay dung lop mo ta ngay thang nam
class date:
    def __init__(seft, day=1, month=1, year=1900):
        seft.day=day
        seft.month=month
        seft.year=year
    def display(seft):
        print(f"{seft.day:2}/{seft.month:2}/{seft.year}")
    def next(seft):
        day_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
        # kiem tra nam nhuan
        if(seft.day%4==0 and seft.day%100!=0) or (seft.day%400==0):
            day_in_month[1]=29# kiem tra thang 2 co phai nam nhuan hay khong
         # tinh ngay tiep theo
        seft.day+=1
        if seft.day>day_in_month[seft.month-1]:
            seft.day=1
            seft.month+=1
            if seft.month>12:
                seft.month=1
                seft.year+=1
# chuong trinh chay
DATE=date(31, 12, 2000)
DATE.display()
DATE.next()
DATE.display()
