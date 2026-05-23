class Circle:
    def Dientich(self):
        return self.bk * self.bk * 3.141592

    def Nhap(self):
        self.bk = float(input("Nhập bán kính: "))

c = Circle()
c.Nhap()
print("Diện tích hình tròn là: ", c.Dientich())