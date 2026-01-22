#Python: Alt+ Shift + e > 해당 선만 실행
#문자열에는 -연산자는 적용 X
#모든 숫자는 0~시작
#win + . = 이모지


# str
# -문자열
# - ', ", ''', """

s="Hello World"
print(s, type(s))

a = """
문자열 주석 아님. 그냥 문자열 값
"""

#연산지 + 이어 붙이기
print(a, type(a))
print('carry')
print('3 ab'*10)

#문자열 (문자 + 배열)
# - 인덱스를 통해 접근 가능
# - 0-based index: 0~ (n-1)
x ='Friday'
print(x[0],x[1],x[2],x[3],x[4],x[5])
# 6글자 자리= 0~5/print(x[6])= index error
print(len(x))
#역인덱스
print(x[-1],x[-2],x[-3],x[-4],x[-5],x[-6])

#sliicing 지원
# - 원하는 구간의 문자열을 추출할 수 있다.
txt = "hello world"
print('txt: 길이', len(txt))
print(txt[0:5:1]) #start~(end-1)
print(txt[0:5]) #step을 생략하면 step=1이 default
print(txt[:5]) #start 생략 = default = 0
print(txt[6:11])
print(txt[::2]) #0 2 4 6 8 10
print(txt[::-1]) #역순

#문자열 불변타임(immutable)
s = 'hello'
print(id(s))


#s = s + ('world')
s += 'world' #s에게 값을 추가해서 다시 s에게
print(s, id(s))

#포맷팅
# - 형식 문자열의 일부를 다른 변수/값으로 치환
# - %
# - str.format()
# - f.string: 3.6ver. ~

x = 10
y = 3.45
print('%d + %.2f = %d'%(x,y,x+y))
print('{} + {} = {}'.format(x,y,x+y))
print(f'{x} + {y} = {x+y}')

# 표현식 = { }넣는 식/하나의 값이 나오게 하는 식,
# 형태로 변수를 활용하여 문자열을 만들수 있음

# str api
# - https://docs.python.org/ko/3.12/library/stdtypes.html#str
# str .replace(old, new)
# - 특정 문자열을 찾아서 원하는 문자열로 치환
today= '2026-1-22'
print(id(today))
today_ = today.replace('-','/') #원본(today)는 두고 새로 문자열을 반환해줌
print(today_)
print(id(today))
print(today_)
#today/today_결과물이 같음 == 원본 데이터는 같음


#str.strip()
# - 시작/끝부분 공백 제거
text= '  하하하   '
print('(',text.strip(),')')



















