class Stack:
    def __init__(self, capacity):
        """Hàm tạo khởi tạo ngăn xếp với kích thước xác định"""
        self.capacity = capacity    # Dung lượng tối đa của ngăn xếp
        self.stack = []             # Dữ liệu là mảng động (list)
        self.size = 0               # Biến lưu kích thước hiện tại của ngăn xếp

    def push(self, value):
        """Phương thức đưa một phần tử vào ngăn xếp"""
        if self.isFull():
            print("Ngăn xếp đã đầy! Không thể thêm phần tử.")
        else:
            self.stack.append(float(value))  # Thêm phần tử vào cuối danh sách
            self.size += 1  # Tăng kích thước ngăn xếp
            print(f"Đã đưa {value} vào ngăn xếp.")

    def pop(self):
        """Phương thức lấy một phần tử ra từ đỉnh ngăn xếp"""
        if self.isEmpty():
            print("Ngăn xếp rỗng! Không thể lấy phần tử.")
            return None
        else:
            value = self.stack.pop()  # Lấy phần tử cuối cùng (đỉnh ngăn xếp)
            self.size -= 1  # Giảm kích thước ngăn xếp
            print(f"Đã lấy {value} ra khỏi ngăn xếp.")
            return value

    def isEmpty(self):
        """Phương thức kiểm tra ngăn xếp có trống không"""
        return self.size == 0

    def isFull(self):
        """Phương thức kiểm tra ngăn xếp đã đầy chưa"""
        return self.size == self.capacity

    def __del__(self):
        """Hàm hủy giải phóng ngăn xếp"""
        print("Giải phóng bộ nhớ ngăn xếp.")
        del self.stack

# Chương trình minh họa
def main():
    # Tạo một ngăn xếp với dung lượng tối đa là 5
    stack = Stack(5)

    # Thử đưa các phần tử vào ngăn xếp
    stack.push(10.5)
    stack.push(20.3)
    stack.push(30.7)
    stack.push(40.1)
    stack.push(50.2)

    # Thử đưa thêm phần tử vào khi ngăn xếp đầy
    stack.push(60.0)  # Ngăn xếp đã đầy

    # Lấy phần tử ra khỏi ngăn xếp
    stack.pop()
    stack.pop()

    # Kiểm tra ngăn xếp trống chưa
    print("Ngăn xếp rỗng?" , stack.isEmpty())

    # Hủy ngăn xếp
    del stack

if __name__ == "__main__":
    main()
