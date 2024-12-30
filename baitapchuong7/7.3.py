import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Cửa sổ với nhãn tùy chỉnh")

# Kích thước cửa sổ
root.geometry("400x300")

# Tạo nhãn với kiểu chữ đậm
label = tk.Label(root, text="Nhãn với kiểu chữ đậm", font=("Arial", 16, "bold"))
label.pack(pady=20)

# Hiển thị cửa sổ
root.mainloop()
