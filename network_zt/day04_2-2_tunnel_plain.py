outer = {"dst": "203.0.113.1", "data": {"dst": "10.10.20.5"}}  # data 칸의 값이 또 딕셔너리인 딕셔너리를 outer 에 담는다
print(outer["dst"])                                             # 바깥 딕셔너리의 dst 를 꺼내 출력한다
print(outer["data"])                                            # data 칸을 꺼내면 안쪽 딕셔너리 통째로 나온다
print(outer["data"]["dst"])                                     # 꺼낸 안쪽 딕셔너리에서 dst 를 한 번 더 꺼내 출력한다

# 203.0.113.1              ← print(outer["dst"])
# {'dst': '10.10.20.5'}    ← print(outer["data"]) — 중괄호가 있는 딕셔너리
# 10.10.20.5               ← print(outer["data"]["dst"])