import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Cửa sổ có nhãn")

# Kích thước cửa sổ
root.geometry("400x300")

# Tạo nhãn
label = tk.Label(root, text="Đây là nhãn của bạn!", font=("Arial", 16))
label.pack(pady=20)

# Hiển thị cửa sổ
root.mainloop()
