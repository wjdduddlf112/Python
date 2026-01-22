#list
# - 컨테이너 자료형
# - list, tuple, dict, set ...
# 저장된 순서를 기억 (인덱스)
# - 슬라이싱 제공

lst = [1,2,3]
print(lst, type(lst))

print(lst[0],lst[1], lst[2])

#list는 요소를 추가.삭제 가능한 mutable(가변) 자료형

lst.append(4)
print(lst, id(lst))

#원하는 인덱스에(위치)에 요소를 추가
lst.insert(1,1.5)
lst.insert(0,0)
print(lst)

#값 변경
lst[0] = -1
print(lst)

#특정 인덱스 값 삭제
lst.pop(2)
print(lst)

del lst[1]
print(lst)

# 2차원 list = 1차원 list를 관리하는 list
students = [['홍길동',20], ['신사임당',22], ['이순신',58]]
print(students)

#인덱싱(차례대로)
print(students[0]) # 첫번째로 관리하는 1차원 리스트
print(students[1])
print(students[1][1]) #두번째로 관리하는 1차원 리스트의 두번째 값
print(students[2][1]) #세번째 관리/2번째 값

#csv 데이터를 list로 관리
# CSV = comma separated value
data = "홍길동, 20, 서울 , 서초구"
print(data)
print(data.split(',')) #spilit은 전달된 구분자를 통해 parsing(짤라서)해서 새로운 list로 반환
data= data.split(',') #원본 변수 바꾸기
print(data)

#변수명 뒤에 _를 넣는 이유
#1. 내가 쓴 변수명과 충돌 방지
#2. 예약어와 충돌 방지
data_ = data
name = data_[0]
age = data_[1]
addr1 = data_[2]
addr2 = data_[3]
print(name, age, addr1, addr2)

# list  반복하며 traversing 가능 = iterable
lst = ['a','b','c']
# for in 반복 문
for v in lst: # - : 필수 입력
    print(v)
# ctrl+z=실행 취소/ctrl+shift+z=앞으로 돌리기

for index,v, in enumerate(lst):
    print(index, v) #index = numbering


#반복 할 때 enumerate에 list를 주면  index도 추출할 수 있다.
for index,v, in enumerate(lst):
    print(index, v)

#더하기/곱하기 연산
    foods = ['🍕'+'🧇']
    drinks = ['🌭']
    print(foods+drinks)
    foods.append(drinks) #foods (원본)에 drinks를 추가해서 foods를 변화시켜
    print(foods)    #변화된 foods를 출력해줘.
    #주의
    print(foods.append(drinks)) #기능마다 반환형이 없는 것도 있고, 호출한 list 원본을 변경하는 것도 존재.
    print(foods*3)


#정렬
# 1. 사전순
fruits = ['orange','apple','banana','kiwi']
print(fruits)

fruits.sort()
print(fruits)

# 역순
fruits.sort(reverse=True)
print(fruits)

# 2. 크기순
nums = [20, 25, 10, -10]
nums.sort(reverse=True)
print(nums)

# key 정렬 기준 함수
fruits.sort(key=len) #len('orange') -> len('apple') -> ...
print(fruits)

# 커스텀 정렬 기준 함수
#my_sort라는 이름에 1. 문자열의 길이, 2. 알파벳 순으로 정렬할 때 사용할 값을 반환하는 함수
def my_sort(elem):
    return len(elem),elem
fruits.sort(key=my_sort)
print(fruits)

fruits=['orange','apple','banana','kiwi']
sorted(fruits)#정렬만
print(fruits)
print(sorted(fruits))
fruits=sorted(fruits) #원본 = 정렬된 걸로 확정
print(fruits)

# 원본을 바꾸는 것을 in-place(sorted() , 안 바꾸는 것 not-in-place(sorted())
# 함수들은 다 다르니까 잘 보고 활용하자

#slicing을 통한 값 변경
texts = ['hello', 'hi', '안녕','곤니치와']
print(texts[:2],type(texts[:2])) #str

texts[1:3] = ['你好','워아이니']
print(texts[1:3]) #list
