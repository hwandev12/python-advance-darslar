
# bitta class ochishimiz kerak bo'ladi
class Number:
    
    # init orqali asosiy hossa uchun x va y ni yozib olishim kerak
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # bu yerda add orqali raqamlarni qoshamiz
    def __add__(self, yangi):
        return Number(self.x + yangi.x, self.y + yangi.y)
        
    # va ohirida hossani aniq chiqarishlik uchun repr dan fodalanaman
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

num1 = Number(10, 10)
num2 = Number(20, 60)
num3 = Number(30, 30)

print(num1 + num2 + num3)