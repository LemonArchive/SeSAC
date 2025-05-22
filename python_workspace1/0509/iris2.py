f = open("iris.csv", "r" , encoding='UTF-8')

class Iris:

    def __init__(self):
        self.my_list = []
        self.value0= 0
        self.value1= 0
        self.value2= 0
        self.value3= 0
        self.aa = 0

    def makelist(self):
        while True: # 데이터 한줄읽고 쪼개고 추가
            self.lines = f.readline().strip()
            if len(self.lines) == 0 :
                break 
                

            result = self.lines.split(',')
            self.my_list.append(result)
        

    def cal(self): #계산
        for value in self.my_list[1:]:
            self.value0 += float(value[0])
            self.value1 += float(value[1])
            self.value2 += float(value[2])
            self.value3 += float(value[3])
            self.aa += 1 #횟수세기 len으로대체가능
    
    def printall(self):
        print(f" {self.value0 / self.aa:.2f}")
        print(f" {self.value1 / self.aa:.2f}")
        print(f" {self.value2 / self.aa:.2f}")
        print(f" {self.value3 / self.aa:.2f}")

if __name__ == "__main__":
    ir = Iris()
    ir.makelist()
    ir.cal()
    ir.printall()
