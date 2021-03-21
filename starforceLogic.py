import random

# # 스타캐치 성공 시 확률 ( 실패 시 확률 x 1.05 )
# successRateStar=[0.9975, 0.9450, 0.8925, 0.8925, 0.84,
#                 0.7875, 0.7350, 0.6825, 0.63, 0.5775,
#                 0.5250, 0.4725, 0.42, 0.3675, 0.3150,
#                 0.3150, 0.3150, 0.3150, 0.3150, 0.3150,
#                 0.3150, 0.3150, 0.0315, 0.021, 0.0105]

# 강화에 필요한 메소
mesoRate=[321000, 641000, 961000, 1281000, 1601000,
         1921000, 2241000, 2561000, 2881000, 3201000,
         12966500, 16400100, 20356300, 24865300, 29956500,
         71316500, 83999600, 98016700, 113422300, 130270000,
         148612400, 168501500, 189988600, 213124000, 237957700]

# 스타캐치 X 확률
successRateNoStar=[0.95, 0.9, 0.85, 0.85, 0.8,
                  0.75, 0.7, 0.65, 0.6, 0.55,
                  0.5, 0.45, 0.4, 0.35, 0.3,
                  0.3, 0.3, 0.3, 0.3, 0.3,
                  0.3, 0.3, 0.03, 0.02, 0.01]

# 파괴확률
destroyRate=[0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0.006, 0.013, 0.014,
            0.021, 0.021, 0.021, 0.028, 0.028,
            0.07, 0.07, 0.2, 0.3, 0.4]

star = 0
failRepeatCount = 0
mesoTotal = 0

while(True):
    command = input("명령어 │ 강화 : 1 │ 종료 : 0\n> ")

    if(command=="0"):
        break

    elif(command=="1"):
        rate = random.random()

        if(failRepeatCount==2):
            print("\n\n찬스타임 발동!! 강화 성공!!!")
            star+=1
            failRepeatCount=0

        elif(rate <= successRateNoStar[star]):
            print("\n\n강화 성공!!")
            star+=1
            failRepeatCount=0

        elif(rate <= successRateNoStar[star]+destroyRate[star]):
            print("\n\n장비가 파괴되었습니다!!!!!!!!")
            star=12
            mesoTotal+=2000000000 # 파괴시 아이템값 20억메소 

        else:
            if(star>10):
                if(star != 15 and star != 20):
                    print("\n\n강화 실패!! ( 스타포스 하락 )")
                    star-=1
                    failRepeatCount+=1
                else:
                    print("\n\n강화 실패!! ( 스타포스 유지 )")
            else:
                print("\n\n강화 실패!! ( 스타포스 유지 )")
        
        mesoTotal += mesoRate[star]

        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n\n")
        print("★  현재 스타포스 수치 :",star,"★\n\n")
        print("총 사용한 메소 :",mesoTotal)
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    else:
        print("잘못된 입력입니다.")
    if(star == 25):
        print("최대 강화 25성 완료! 축하드립니다.")
        break
