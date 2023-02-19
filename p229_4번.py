cha = {
    "name": "기사",
    "level": 12,
    "items":{
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}


for key in cha:
    if type(cha[key]) is dict:   # (2) 요소의 값이 딕셔너리(items)일 때
        # print(cha[key])  # cha[key]에 딕셔너리 들어옴
        for 템 in cha[key]:  # (4) 딕셔너리 기반으로 반복 돌 것
            print(f'{템} : {cha[key][템]}')

    elif type(cha[key]) is list:  # (3) 요소의 값이 리스트(skill)일 때
        # print(cha[key])  # cha[key]에 리스트 들어옴
        for 스킬 in cha[key]:  # (5) 리스트 기반으로 반복 돌 것
            print(f'skill : {스킬}')

    else:
        print(f'{key} : {cha[key]}')  # (1) 다 출력해봐
