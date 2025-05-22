# 회원관리 - 회원번호, 회원아이디, 패스워드, 이름, 전화번호, 이메일
# 게시판  - 회원번호, 글번호, 제목, 내용, 작성일 , 조회수

# 회원가입 수정 탈퇴, 조회(자기정보)
# 게시글 작성 - 회원번호, 제목, 내용, 작성일(date), 조회수 0
#     읽어보기
#     수정(글쓴이만) 회원번호 패스워드 입력하면
#     삭제(글쓴이만) 회원번호 패스워드 입력하면
import datetime
import pickle
class Forumuser:
    
    def __init__(self):
        
        self.member_list = []        
        self.member_id_counter = 1 
        
    def register(self):
        member = {}
        print("회원가입을 진행하겠습니다.")
        member["num"] = self.member_id_counter
        member["id"] = input("아이디를 입력해주세요 : ")
        for dup in self.member_list:# id 중복방지
            if dup["id"] == member["id"]:
                print("다른 id를 사용해주세요")
                return
        member["pw"] = input("비밀번호를 입력해주세요 : ")
        member["name"]= input("이름을 입력해주세요 : ")
        member["phone"] = input("전화번호를 입력해주세요 : ")
        member["email"] = input("이메일을 입력해주세요 : ")
        self.member_list.append(member)
        self.member_id_counter += 1
     
        print(f"회원가입 되었습니다. {member['id']}님의 회원번호는 {member['num']}입니다")

    def save_members(self, filename="members.txt"):
        with open(filename, "wb") as f:
    
            pickle.dump(self.member_list, f)
            print(f"회원목록이 {filename}에 저장되었습니다.")

    def load_members(self, filename="members.txt"):
        try:
            with open(filename, "rb") as f:
                self.member_list = pickle.load(f)
            print(f"{filename}에서 회원목록을 불러왔습니다.")
            if self.member_list:
                self.member_id_counter = max(mem["num"] for mem in self.member_list) + 1
            else:
                self.member_id_counter = 1
        except: print("불러오기 오류")

    def member_update(self):# 아디 입력후 리스트에서 사람선택후 비밀번호가 동일하다면
        found = False                 # 정보수정 : 아이디 비번 이름 번호 이메일을 입력받는다.
        print("정보수정")
        inputid = input("아이디를 입력해주세요")
        inputpw = input("비밀번호를 입력해주세요")

        
        for mem in self.member_list:
            if inputid == mem["id"] and inputpw == mem["pw"]:
                found = True
                mem["id"] = input("아이디를 입력해주세요 : ")
                for dup in self.member_list:# id 중복방지
                    if dup["id"] == mem["id"]:
                        print("다른 id를 사용해주세요")
                        return
                mem["pw"] = input("비밀번호를 입력해주세요 : ")
                mem["name"]= input("이름을 입력해주세요 : ")
                mem["phone"] = input("전화번호를 입력해주세요 : ")
                mem["email"] = input("이메일을 입력해주세요 : ")
                print(f"{mem['name']}님의 정보수정이 완료되었습니다. ")
                return
        if not found:
            print("잘못된 입력입니다.")

    def member_profile(self):# 정보조회
        found = False       
        print("내 정보보기")           
        inputid = input("아이디를 입력해주세요")
        inputpw = input("비밀번호를 입력해주세요")
        for mem in self.member_list:
            if inputid == mem["id"] and inputpw == mem["pw"]:
                found = True
                print(f"회원번호 : {mem['num']}")
                print(f"아이디 : {mem['id']}")
                print(f"이름 : {mem['name']}")
                print(f"전화번호 : {mem['phone']}")
                print(f"이메일 : {mem['email']}")        
                return     

        if not found:
            print("잘못된 입력입니다.")

    def admin_login(self):
        apw= int(input("비밀번호를 입력해주세요 "))
        if apw == 4646: #원래 는 절대 비밀번호를 하드코딩하면안되지만 관리자등록까지는...
           self.admin_main()
        else : print("로그인실패")

    def admin_main(self):
        print("관리자 페이지")
        print("1. 회원 전체 조회")
        print("2. 회원 강제 탈퇴")
        print("0. 돌아가기")
        choice = input("원하는 작업을 선택하세요 : ")

        if choice == "1":
            self.memberprint()
        elif choice == "2":
            self.admin_userdel()
        elif choice == "0":
            return
        else:
            print("잘못된 입력입니다.")
   

    def admin_userdel(self):
        print("강제 탈퇴할 회원의 회원번호를 입력하세요.")
        try:
            del_num = int(input("회원번호: "))
            for mem in self.member_list:
                if mem["num"] == del_num:
                    self.member_list.remove(mem)
                    print(f"{mem['id']} 회원이 강제 탈퇴되었습니다.")
                    return
        except: print("해당 회원번호를 찾을 수 없습니다.")

    def member_delete(self): # 아디 비번 입력받은후 정말삭제하시겠습니까? y 입력시 리스트에서 삭제
        found = False
        print("회원탈퇴")
        inputid = input("아이디를 입력해주세요")
        inputpw = input("비밀번호를 입력해주세요")
        for mem in self.member_list:
            if inputid == mem["id"] and inputpw == mem["pw"]:
                found = True 
                yn = input("정말 삭제하시겠습니까? y / n")
                if yn == "y" or yn == "Y":
                    self.member_list.remove(mem)
                    print(f"{mem['id']} 님의 회원탈퇴가 완료되었습니다.")
                    return
                else : 
                    print("회원탈퇴를 취소합니다.")
        if not found:
            print("잘못된 입력입니다.")
        
    def memberprint(self):
        print("회원 목록")
        for mem in self.member_list:
            print(f"[회원번호: {mem['num']}] 아이디: {mem['id']}, 이름: {mem['name']}, 전화: {mem['phone']}, 이메일: {mem['email']}")


    

class ForumBoard(): #게시판  - 회원번호, 글번호, 제목, 내용, 작성일 , 조회수
     
    def __init__(self):
        self.post_list = []
        self.post_num = 1
        self.post_count = 0
        
        
    def write_post(self, member_list): #포스트작성
        post= {}
        dt = datetime.datetime.now() 
        dtf = dt.strftime("%Y-%m-%d %H:%M:%S")
        
        id_input = input("아이디를 입력해주세요: ")
        pw_input = input("비밀번호를 입력해주세요: ")

        member = next((m for m in member_list if m["id"] == id_input and m["pw"] == pw_input), None)
        if not member:
            print("회원 인증 실패")
            return
           
        post['post_num'] = self.post_num
        post['id'] = input("이름을 입력해주세요")
        post['title'] = input("제목을 입력해주세요")
        post['detail'] = input("내용을 입력해주세요")
        post['time'] = dtf
        post["count"] = 0
        post['pw'] = pw_input
        
        self.post_list.append(post)
        self.post_num += 1
        self.post_count += 1
        print("작성 완료")

    def save_posts(self, filename="posts.txt"):
        with open(filename, "wb") as f:
            pickle.dump((self.post_list, self.post_num), f)
            print(f"게시글이 {filename}에 저장되었습니다.")

    def load_posts(self, filename="posts.txt"):
        try:
            with open(filename, "rb") as f:
                self.post_list, self.post_num = pickle.load(f)
            print(f"{filename}에서 게시글을 불러왔습니다.")
        except:
            print("게시글 불러오기 오류")

    def list_posts(self):
        if not self.post_list:
            print("등록된 게시글이 없습니다.")
            return
        print("글 목록")
        for post in self.post_list:
            print(f"{post['post_num']}. [{post['title']}] - 작성자: {post['id']} / 작성일: {post['time']} / 조회수: {post['count']}")


    def view_post(self):
        try:
            post_id = int(input("조회할 글 번호를 입력하세요: "))
            post = next((p for p in self.post_list if p['post_num'] == post_id), None)
            if not post:
                print("해당 글이 존재하지 않습니다.")
                return
            post["count"] += 1
            print(f"\n제목: {post['title']}")
            print(f"작성자: {post['id']}")
            print(f"작성일: {post['time']}")
            print(f"조회수: {post['count']}")
            print(f"내용:\n{post['detail']}\n")
        except:
            print("잘못된 입력입니다.")   

    def delete_post(self):
        try:
            post_id = int(input("삭제할 글 번호를 입력하세요: "))
            post = next((p for p in self.post_list if p['post_num'] == post_id), None)
            if not post:
                print("해당 글이 존재하지 않습니다.")
                return

            id_input = input("아이디 입력: ")
            pw_input = input("비밀번호 입력: ")
            if post["id"] == id_input and post["pw"] == pw_input:
                self.post_list.remove(post)
                print("게시글이 삭제되었습니다.")
            else:
                print("삭제실패")
        except:
            print("입력 오류")

    def admin_delete_post(self):
        admin_pw = input("관리자 비밀번호 입력: ")
        if admin_pw != "4646":
            print("관리자 인증 실패")
            return
        try:
            post_id = int(input("삭제할 글 번호를 입력하세요: "))
            post = next((p for p in self.post_list if p['post_num'] == post_id), None)
            if not post:
                print("해당 글이 존재하지 않습니다.")
                return
            self.post_list.remove(post)
            print("삭제완료")
        except:
            print("입력 오류")    

def main():
    user_manager = Forumuser()
    board_manager = ForumBoard()

    
    user_manager.load_members()
    board_manager.load_posts()

    while True:
        print("1. 회원가입")
        print("2. 정보 확인")
        print("3. 회원 정보 수정")
        print("4. 회원 탈퇴")
        print("5. 관리자 로그인")
        print("6. 게시글 목록 보기")
        print("7. 게시글 상세 보기")
        print("8. 게시글 작성")
        print("9. 게시글 삭제")
        print("10. 관리자 게시글 삭제")
        print("0. 종료 및 저장")
        choice = input("숫자를 입력해주세요 ")

        if choice == "1":
            user_manager.register()
        elif choice == "2":
            user_manager.member_profile()
        elif choice == "3":
            user_manager.member_update()
        elif choice == "4":
            user_manager.member_delete()
        elif choice == "5":
            user_manager.admin_login()
        elif choice == "6":
            board_manager.list_posts()
        elif choice == "7":
            board_manager.view_post()
        elif choice == "8":
            board_manager.write_post(user_manager.member_list)
        elif choice == "9":
            board_manager.delete_post()
        elif choice == "10":
            board_manager.admin_delete_post()
        elif choice == "0":
            print("저장 중...")
            user_manager.save_members()
            board_manager.save_posts()
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")

# 실행
if __name__ == "__main__":

    main()



        



