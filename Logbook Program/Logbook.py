#TODO GUI 개발
#TODO 시간입력 자동화
A=10

while A==10:
  select=input("로그 등록은 1, 로그 조회는 2, 종료는 9를 입력하세요\n:")
  select=int(select)

  if select==1 :
    A=10
    print("\n로그 등록을 선택하셨습니다.\n로그 등록을 위해 다음 정보들을 입력해 주세요.\n")

    callsign=input("교신 상대국 콜사인을 입력해 주세요:").upper()
    month=input("교신시 월을 입력해 주세요:")
    day=input("교신시 일을 입력해 주세요:")
    hour=input("교신 시간 시를 KST기준으로 입력해 주세요(24시간기준):")
    minute=input("교신 시간 분을 KST 기준으로 입력해 주세요:")
    rxrs=input("상대국 신호를 입력해 주세요:")
    txrs=input("본인 신호를 입력해 주세요:")

    txt=open("log.txt", "a")
    txt.write("\n"+callsign+"\n")
    txt.write(month+"\n")
    txt.write(day+"\n")
    txt.write(hour+"\n")
    txt.write(minute+"\n")
    txt.write(rxrs+"\n")
    txt.write(txrs+"\n")
    txt.close()
    print(callsign+"국과의 교신이 기록되었습니다.\n")
    print("-----------------------------------")

  if select==2:
    A=10
    print("\n로그 조회를 선택하셨습니다.\n")
    print("콜사인으로 검색하려면 1, 날짜로 검색하려면 2를 입력해 주세요.\n:")
    searchsel=int(input())
    if searchsel==1:
      callsign=input("교신 상대국 콜사인을 입력해 주세요:").upper()
      txt=open("log.txt", "r")
      call=txt.readlines()
      TOF=False
      for a in range(0, len(call)):
        if(call[a]==callsign+"\n"):
          TOF=True
          calls=call[a].replace("\n", "")
          month=call[a+1].replace("\n", "")
          day=call[a+2].replace("\n", "")
          hour=call[a+3].replace("\n", "")
          minute=call[a+4].replace("\n", "")
          rxrs=call[a+5].replace("\n", "")
          txrs=call[a+6].replace("\n", "")
          print("-----------------------------------")
          print("         "+month+"월 "+day+"일 "+hour+"시 "+minute+"분"+"            \n"+"               "+calls+"                          \n"+"      "+"수신감도:" +rxrs+" | "+"송신감도: "+txrs)
    
    if searchsel==2:
      month=input("교신시 월을 입력해 주세요:")
      day=input("교신시 일을 입력해 주세요:")
      txt=open("log.txt", "r")
      call=txt.readlines()
      TOF=False
      for a in range(0, len(call)):
        if(call[a]==month+"\n"):
          if(call[a+1]==day+"\n"):
            TOF=True
            calls=call[a-1].replace("\n", "")
            month=call[a].replace("\n", "")
            day=call[a+1].replace("\n", "")
            hour=call[a+2].replace("\n", "")
            minute=call[a+3].replace("\n", "")
            rxrs=call[a+4].replace("\n", "")
            txrs=call[a+5].replace("\n", "")
            print("-----------------------------------")
            print("         "+month+"월 "+day+"일 "+hour+"시 "+minute+"분"+"            \n"+"               "+calls+"                          \n"+"      "+"수신감도:" +rxrs+" | "+"송신감도: "+txrs)
    print("-----------------------------------\n")
    if not TOF:
      print("교신기록이 없습니다.+'\n'")
    txt.close()
  
  if select==9:
    print("종료합니다.")
    A=11