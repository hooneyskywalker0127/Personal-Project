

feeling = input("오늘 기분이 어떤가요? 1. 행복 2. 우울")
if feeling == '행복' or feeling == '1':
    print('햄버거')
elif feeling == '우울' or feeling == '2':
    print('울면')
else:
    print('행복 or 슬픔으로 입력하세요')