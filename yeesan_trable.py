class daily_trip:
    def __init__(self,course):
        self.course = course

    def daily(self):
        """
        course 1 == traditional trip
        course 2 == national trip
        course 3 == healing trip 
        """
        # course 1 - Traditional
        if self.course == '1':
            print("역사 코스를 선택하셨군요!")
            print("역사 코스는 2가지로 나뉘어져 있습니다.")
            course_num = input("어떤 코스로 안내해 드릴까요?\n1. 1번 코스 \t 2. 2번 코스 \t 3. 두가지 다\n")
            print()
            if course_num == '1':
                print("역사 1번 코스에 대해서 안내드리겠습니다.")
                strFormat = '%-30s%-30s%-30s\n'
                strOut = strFormat % ('시간','내용','비고')

                with open('./Data/Traditional/daily_traditional_1.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
            elif course_num == '2':
                print("역사 2번 코스에 대해서 안내드리겠습니다.")
                strFormat = '%-30s%-30s%-30s\n'
                strOut = strFormat % ('시간','내용','비고')

                with open('./Data/Traditional/daily_traditional_2.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
            elif course_num == '3':
                print("먼저 역사 1번 코스에 대해서 안내드리겠습니다.")
                strFormat = '%-30s%-30s%-30s\n'
                strOut = strFormat % ('시간','내용','비고')
                # 1번 코스에 대한 것 
                with open('./Data/Traditional/daily_traditional_1.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
                print()
                # 2번 코스에 대한 것
                print("다음으로 2번 코스입니다.")
                with open('./Data/Traditional/daily_traditional_2.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
            else:
                print('없는 번호 입니다. 다른 번호를 선택해주세요')
                exit()

        # course 2 - National
        if self.course == '2':
            print("생태 코스를 선택하셨군요!")
            print("생태 코스는 3가지로 나뉘어져 있습니다.")
            course_num = input("어떤 코스로 안내해 드릴까요?\n1. 1번 코스 \t 2. 2번 코스 \t 3. 3번 코스 \t 4. 모든 코스\n")
            print()
            if course_num == '1':
                print("생태 1번 코스에 대해서 안내드리겠습니다.")
                strFormat = '%-30s%-30s%-30s\n'
                strOut = strFormat % ('시간','내용','비고')

                with open('./Data/National/daily_national_1.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
            elif course_num == '2':
                print("생태 2번 코스에 대해서 안내드리겠습니다.")
                strFormat = '%-30s%-30s%-30s\n'
                strOut = strFormat % ('시간','내용','비고')

                with open('./Data/National/daily_national_2.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
            elif course_num == '3':
                print("생태 3번 코스에 대해서 안내드리겠습니다.")
                strFormat = '%-30s%-30s%-30s\n'
                strOut = strFormat % ('시간','내용','비고')

                with open('./Data/National/daily_national_3.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
            elif course_num == '4':
                print("먼저 생태 1번 코스에 대해서 안내드리겠습니다.")
                strFormat = '%-30s%-30s%-30s\n'
                strOut = strFormat % ('시간','내용','비고')

                with open('./Data/National/daily_national_1.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
                print()
                print("다음으로 2번 코스에 대해서 안내드리겠습니다.")
                strFormat = '%-30s%-30s%-30s\n'
                strOut = strFormat % ('시간','내용','비고')

                with open('./Data/National/daily_national_2.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
                print()
                print("마지막으로 3번 코스에 대해서 안내드리겠습니다.")
                strFormat = '%-30s%-30s%-30s\n'
                strOut = strFormat % ('시간','내용','비고')

                with open('./Data/National/daily_national_3.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
                print()
            else:
                print('없는 번호 입니다. 다른 번호를 선택해 주세요')
                exit(-1)
                
        # course 3 - Healing
        if self.course == '3':
            print("힐링 코스를 선택하셨군요!")
            print("힐링 코스는 2가지로 나뉘어져 있습니다.")
            course_num = input("어떤 코스로 안내해 드릴까요?\n1. 1번 코스 \t 2. 2번 코스 \t 3. 두가지 다\n")
            print()
            if course_num == '1':
                print("힐링 1번 코스에 대해서 안내드리겠습니다.")
                strFormat = '%-30s%-30s%-30s\n'
                strOut = strFormat % ('시간','내용','비고')

                with open('./Data/Healing/daily_headling_1.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
            elif course_num == '2':
                print("힐링 2번 코스에 대해서 안내드리겠습니다.")
                strFormat = '%-30s%-30s%-30s\n'
                strOut = strFormat % ('시간','내용','비고')

                with open('./Data/Healing/daily_healing_2.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
            elif course_num == '3':
                print("먼저 힐링 1번 코스에 대해서 안내드리겠습니다.")
                strFormat = '%-30s%-30s%-30s\n'
                strOut = strFormat % ('시간','내용','비고')
                # 1번 코스에 대한 것 
                with open('./Data/Healing/daily_healing_1.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
                print()
                # 2번 코스에 대한 것
                print("다음으로 2번 코스에 대해서 안내드리겠습니다.")
                with open('./Data/Healing/daily_healing_2.txt', 'r', encoding='utf-8') as f:
                    for x in f.readlines():
                        y = x.split('\t')
                        strOut += strFormat %(y[0],y[1],y[2].rstrip())
                print(strOut)
            else:
                print('없는 번호 입니다. 다른 번호를 선택해주세요')
                exit()  