def solution(dots):
    answer = 0
    a1 = (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0])
    a2 = (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0])
    
    b1 = (dots[0][1] - dots[2][1]) / (dots[0][0] - dots[2][0])
    b2 = (dots[1][1] - dots[3][1]) / (dots[1][0] - dots[3][0])
    
    c1 = (dots[0][1] - dots[3][1]) / (dots[0][0] - dots[3][0])
    c2 = (dots[1][1] - dots[2][1]) / (dots[1][0] - dots[2][0])
    
    if a1 == a2 or b1 == b2 or c1 == c2:
        return 1       
    return answer