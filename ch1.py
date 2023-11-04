qa = {"취존" : "취향존중",
      "솔까말" : "솔직히 까놓고 말해서",
      "케바케" : "케이스 바이 케이스"
      }
      
num_qa = len(qa)
answer_cnt = 0      
# 반복문을 통해 
print("안녕하세요! 신조어,줄임말 퀴즈를 시작하겠습니다.")
for question, answer in qa.items():
    user_input = input(f"{question}은 어떤 문장의 줄임말인가요? : ").strip()
    
    # 정답이 같으면 정답 카운트 증가
    if user_input == answer:
        print("정답입니다!")
        answer_cnt += 1
    else:
        print("오답입니다")
        
print(f"{num_qa}개 퀴즈 중 {answer_cnt}개 정답")