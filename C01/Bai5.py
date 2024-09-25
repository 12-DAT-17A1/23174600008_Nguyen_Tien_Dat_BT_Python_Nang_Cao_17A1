class Stack:
    def __init__(self,max_size) -> None:
        self.stack = []
        self.max_size  = max_size
    def isEmpty(self):
        return len(self.stack) == 0
    def isFull(self):
        return len(self.stack) == self.max_size
    def push(self,value):
        if self.isFull():
            print('Stack đã đầy!')
        else:
            self.stack.append(float(value))
    def pop(self):
        if self.isEmpty():
            print('Ngăn xếp  trống')
            return
        else:
            return self.stack.pop()
    def count(self):
        #Trả về số lượng phần tử hiện có trên ngăn xếp.
        return len(self.stack)
    def __del__(self):
        print('Giải phóng bộ nhớ ngăn xếp')
    
    
# Ví dụ sử dụng:
stack = Stack(3)  # Khởi tạo ngăn xếp với kích thước tối đa là 3

# Thêm phần tử vào ngăn xếp
stack.push(1.5)
stack.push(2.7)
stack.push(3.9)

# Kiểm tra trạng thái đầy của ngăn xếp
print("Ngăn xếp đã đầy chưa?", stack.isFull())  # True

# Thử thêm phần tử khi ngăn xếp đã đầy
stack.push(4.2)  # Sẽ in ra "Ngăn xếp đã đầy!"

# Lấy phần tử ra từ ngăn xếp
print("Phần tử lấy ra:", stack.pop())  # 3.9

# Kiểm tra trạng thái trống của ngăn xếp
print("Ngăn xếp có trống không?", stack.isEmpty())  # False

print('Số lượng phần tử có trong stack là:',stack.count())
# Xóa ngăn xếp
del stack
