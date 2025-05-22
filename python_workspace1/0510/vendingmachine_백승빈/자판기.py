#자판기 => 객제지향

#: 입력 : 돈(종류별로)카드? 음료주문?
#: 출력 : 음료 , 거스름돈(요즘돈안써요...) 
import random
class Vendingmachine:
    
    def __init__(self):
        self.money = 0
        self.product_list=[]
        self.drink = 0
        self.card = 0
        self.im = 0
        self.value = []
        self.product_display_list = []
        self.product_load()

    def insert_money(self):
        while True:
            im = int(input("현금결제는 1, 카드결제는 2를 눌러주세요"))
            if im == 1:
                self.insert_coin()
                break
                
            elif im == 2: 
                self.card_()
                break
            else: 
                print("다시 입력해주세요")
   
    def insert_coin(self):#돈투입
        while True:
            print("돈을 투입해주세요.")
            coin = int(input())
            print (f" {coin}원 투입되었습니다.")
            self.money += coin
            print (f" 총 투입하신금액 {self.money}원 ")
            return
        
    def card_(self):# 단순 재미용 쓸모없는 카드인식 50퍼확률로 인식불가
        while True:
            a = random.randint(1,10)
            input("결제하실 카드를 단말기에 태그하거나 삽입해 주시고 아무 값이나 입력해주세요")#카드인식위한대기
            if a < 6 :
                self.card = 0
                print("카드인식 오류") 

            else : 
                self.card = 1
                print("카드결제가 활성화되었습니다.") 
                return
            
    def product_load(self):#상품목록 불러오기

        with open("product.csv", "r", encoding='UTF-8') as f:
            while True:
            
                lines = f.readline().strip()
                if len(lines) == 0 :
                    break

                result = lines.split(',')
                self.product_list.append(result)
        f.close()
        
    def product(self):
        self.product_display_list.clear()
        for idx , i in enumerate(self.product_list ,start= 1):

            self.drink = (i[0])
            self.price = int(i[1])
            self.stock = int(i[2])            
            self.product_display_list.append([idx, self.drink, self.price, self.stock])
            print(self.product_display_list)
        
    def purchase(self):
        self.product()
        print(f"투입한 금액 : {self.money}")  
        while True:            
            for item in self.product_display_list:
                print(f"{item[0]}. 제품 : {item[1]} 가격 : {item[2]} 재고 : {item[3]}")
            
            self.choice = int(input(f"구매할 상품을 선택해주세요. 0 을입력하면 종료됩니다."))
            if self.choice == 0:
                break
            
            result = list(filter(lambda w: w[0] == self.choice, self.product_display_list))
            
            for w in result:

                if w[3] == 0:  #오류처리
                    print("재고가 부족합니다.")
                    
                if self.money <= w[2] and self.card == 0: #오류처리
                    print("잔액이 부족합니다.")
                    
                if self.card == 1 and w[3] > 0:
                    print(f"{w[1]} 를 구매합니다.")
                    print(f"{w[2]} 원이 결제되었습니다.")
                    w[3] -= 1

                elif self.money >= w[2] and w[3] > 0:
                    print(f"{w[1]} 를 구매합니다.")
                    self.money -= w[2]
                    w[3] -= 1
                    print(f"남은금액 {self.money}")
                    return
                    #w[2] = 가격
                    #w[3] = 재고

    def change(self):
        print(f"잔돈은 : {self.money}원 입니다.")

    def main_menu(self):
        print("1.돈 투입")
        print("2.구매하기")
        print("3.잔돈받기")
        print("0.종료하기")

    def start(self):
        #함수주소를 배열에 저장하고 호출함 , 
        funcList = ["",self.insert_money,self.purchase, 
                    self.change]
        while True:
            self.main_menu()
            choice = int(input("선택 : "))
            if choice > 0 and choice < len(funcList):
                funcList[choice]()
            elif choice == 0:
                return
            else :
                print("잘못입력하셨습니다.")
            
if __name__ == "__main__":
    v = Vendingmachine()
    v.start()