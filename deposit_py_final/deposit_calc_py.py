#목돈 예치 후 만기시 받는 금액 계산
#Input: 예치액, 예치기간, 이자구분(단/복리), 이자율
#Output: 소득에 대한 과세와 주민세 제외 금액 산출.

import pickle
import os

result=open("result.txt", "w", encoding='UTF8')

capital=int(input("원금 입력: "))
duration=int(input("예치기간 입력(월): "))
interchoice=input("단리는 1, 복리는 2 입력: ")
inter_minmax=input("기본 금리는 1, 최고 금리는 2 입력: ")


with open("name_list.pkl","rb") as n:
    name_list = pickle.load(n)
with open("bank_list.pkl","rb") as b:
    bank_list = pickle.load(b)


for i in range(len(name_list)):
    try:
        if int(inter_minmax)==1:
            with open("basic_list.pkl","rb") as bi: #pkl형태의 list 파일 불러오기
                basic_list = pickle.load(bi)

            basic_inter=float(basic_list[i].replace("기본 금리: ","").replace("%","")) #list에서 계산 하기 위해 기본 금리의 실수만 추출

            inter_calc=basic_inter #결과값 출력시 사용하기 위해 다른 변수에 금리 입력
            inter=inter_calc/100/12 #월 이자율 계산을 위해 12로 나누고 백분율료 되어 있기에 100으로 나눔
            
            if int(interchoice)==1: #단리 계산
                total=float(capital+(capital*inter*duration))
            
            elif int(interchoice)==2: #복리 계산
                total=float(capital*(1+inter)**duration)


        elif int(inter_minmax)==2:
            with open("max_list.pkl","rb") as mi: #pkl형태의 list 파일 불러오기
                max_list = pickle.load(mi)
            
            max_inter=float(max_list[i].replace("최대 금리: ","").replace("%","")) #list에서 계산 하기 위해 기본 금리의 실수만 추출

            inter_calc=max_inter #결과값 출력시 사용하기 위해 다른 변수에 금리 입력
            inter=inter_calc/100/12 #월 이자율 계산을 위해 12로 나누고 백분율료 되어 있기에 100으로 나눔
            
            if int(interchoice)==1: #단리 계산
                total=float(capital+(capital*inter*duration))

            elif int(interchoice)==2: #복리 계산
                total=float(capital*(1+inter)**duration)


        inter_out = total - capital; #총 금액에서 원금을 제해 이자만 추출
        tax_out = inter_out * 15.4 / 100; #이자에 적용되는 세금을 계산
        total=total-tax_out #총 금액에서 세금을 제함

        result.write(str()+str(i+1)+"번째 상품"+"\n")
        result.write(str()+bank_list[i]+"\n")
        result.write(str()+name_list[i]+"\n")
        result.write(str()+"예치 기간: "+str(duration)+"개월"+"\n")
        result.write(str()+"예치 원금: "+str(capital)+"원"+"\n")
        result.write(str()+"환급금: "+str(total)+"원"+"\n")
        result.write(str()+"이율: "+str(inter_calc)+"%"+"\n")
        result.write(str()+"예치 이자: "+str(inter_out)+"원"+"\n")
        result.write(str()+"이자 과세: "+str(tax_out)+"원"+"\n")
        result.write(str()+"----------------------"+"\n")

        #--------------temp for test-----------------
        # name=name_list[i].replace("상품명:  ","")
        # bank_name=bank_list[i].replace("은행명: ","")
        # print(f"상품명: {name}, 은행명: {bank_name}, 예치기간: {duration}개월, 환급금: {total}원, 예치원금: {capital}원, 예치이자: {inter_out}원, 이자 과세: {tax_out}원")
        #--------------temp for test-----------------
    except:
        pass

print("계산 완료")
print("계산 결과는 result.txt에 저장되었습니다.")

result.close()
os.system("pause")