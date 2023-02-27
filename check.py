def solution(cards1, cards2, goal): 
    answer='yes'
    index1,index2=0,0
    for word in goal: # i = 'i'/'want'/'to'/'drink'/'water' 
        if index1<len(cards1) and word==cards1[index1] :
            index1+=1
        elif index2<len(cards2) and word==cards2[index2]:
            index2+=1
        else:
            answer='no'
            break
    return answer

cards1 = ["i", "drink", "water"] 
cards2 = ["want", "to"] 
goal = ["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal)) 

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal)) 