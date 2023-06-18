# 원하시는 선택지를 골라주세요
# 1. 추천테마여행 2. 예산여행지도 3. 미정

# # 추천 테마 여행을 선택 시
# 추천 테마 여행을 고르셨군요 !
# 여행일을 선택해주세요.
# 1. 당일 2. 1박 2일 3. 2박 3일



# # 당일 코스 
import yeesan_trable as yt


category = input("""원하시는 선택지를 골라주세요.\n1. 추천테마여행 \t 2. 예산여행지도\n""")
print()

# 추천 테마 여행을 골랐을 경우
if category == '1':
    print('추천 테마 여행을 고르셨군요!')

    trable_date = input("""여행일을 선택해주세요.\n1. 당일여행 \t 2. 1박 2일 \t 3. 2박 3일 \n""")
elif category == '2':
    print('현재 작업 중입니다')
    exit(-1)
else:
    print('없는 번호 입니다. 다시 선택해주세요')
    exit(-1)
print()


# 여행일에 따른 분리
if trable_date == '1': # 당일치기인 경우
    print("당일 여행을 계획 중이시군요!")
    print("당일 여행 추천 테마 3가지 중 하나를 선택해주세요.")
    daily_corse = input("1. 역사코스 \t 2. 생태코스 \t 3. 힐링코스 \n")
    print()

    # 역사 코스인 경우
    if daily_corse == '1':
        daily_ = yt.daily_trip(daily_corse)
        daily_.daily()
    elif daily_corse == '2':
        daily_ = yt.daily_trip(daily_corse)
        daily_.daily()
    elif daily_corse == '3':
        daily_ = yt.daily_trip(daily_corse)
        daily_.daily()
    else:
        print("없는 번호 입니다. 다른 번호를 선택해 주세요.")
        exit(-1)