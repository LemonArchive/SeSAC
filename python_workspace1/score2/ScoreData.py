from sqlalchemy import text
from DBengine import theEngine

# orm을 사용할때는 클래스를 만들어놓고 쓰는것이 맞음
class ScoreData:
    #db에서 레코드셋 가져왔을떄, ScoreData 객체로 만들어서
    #따로 관리할수있다
    # select ... (kor+eng+mat) total
    def __init__(self, sname="", kor=0, eng=0,mat=0,total=0,average=0,grade=""):
        self.sname = sname
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.total = total
        self.average = average
        self.grade = grade

    def process(self):
        self.total = self.kor+self.eng+self.mat
        self.average = self.total / 3
        if self.average >= 90:
            self.grade = '수'
        elif self.average >= 80:
            self.grade = '우'
        elif self.average >= 70:
            self.grade = '미'
        elif self.average >= 60:
            self.grade = '양'
        else : self.grade = '가'
    def output(self):
        print(f"{self.sname}\t",end="")
        print(f"{self.kor}\t",end="")
        print(f"{self.eng}\t",end="")
        print(f"{self.mat}\t",end="")
        print(f"{self.total}\t",end="")
        print(f"{self.average:.2f}\t",end="")
        print(f"{self.grade}")

    
        
if __name__ == "__main__":

    with theEngine.begin() as conn:
        sql = "select * from tb_score"
        result = conn.execute(text(sql))
        
        for r in result.mappings().all():
            s = ScoreData(r["sname"],r["kor"],r["eng"],r["mat"])
            s.process()
            s.output()
            
