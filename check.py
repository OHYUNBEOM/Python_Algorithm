def solution(cards1, cards2, goal): 
    for i in goal: # i = 'i'/'want'/'to'/'drink'/'water' 
        if i==cards1[0]: # i want to drink water을 cards1,cards2을 연속시켜 조합해서 만들수있는지 확인해야하기에 cards1과cards2의 첫번째 원소랑 계속 같아야 연속해서 만들수있는거임
            cards1.pop(0)#cards1.pop(0)으로 제일 앞에있는 원소를 계속 뽑아옴 
            if len(cards1)==0:
                continue
        elif i==cards2[0]:
            cards2.pop(0)
            if len(cards2)==0:
                break
        else:
            return 'No'
    return 'Yes'

cards1 = ["i", "drink", "water"] 
cards2 = ["want", "to"] 
goal = ["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal)) 

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal)) 