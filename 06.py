#tuple
# -변경 불가한(immutable) list
# - 저장 순서 기억

t1 = () #빈 튜플
#t1 = (10) #값이 하나일 때는 끝에 콤마(,)를 반드시 찍어줘야 한다.
t2= (10,)
t3= (10,20)
t4= 10, 20
print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
print(t4, type(t4))

#읽기 전용
# -indexing
# -slicing
tpl = ('a','b','c','d')
print(tpl[0], tpl[1], tpl[2], tpl[3])
print(tpl[:3])

tpl_ = 'A'  ,tpl[1] ,tpl[2] ,tpl[3]
print(tpl_, type(tpl_))

tpl_ = 'A', *tpl[:1] # *(별표, asterisk)를 활용하면 요소를 흩뿌린다. (언패킹 연산자)
print(tpl_, type(tpl_))

#튜플 언패킹
a = 100
b= 200
print(a, b)

# 꼭 *를 쓰지 않더라도 좌항에 변수 2개 이상에 값을 담을 때도 언패킹이라고 한다.
a, b = 100, 200
print(a, b)

#값 교환
x, y = 88, 99
print(f'x = {x}, y = {y}')
x, y = y, x
print(f'x = {x}, y = {y}')

