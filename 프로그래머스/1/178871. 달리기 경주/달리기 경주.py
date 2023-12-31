def solution(players, callings):
    result = {player: i for i, player in enumerate(players)} # 선수: 등수
    for call in callings:
        idx = result[call] # 호명된 선수의 현재 등수
        result[call] -= 1 # 하나 앞 등수로 바꿔줌 -1
        result[players[idx-1]] += 1 # 앞에 위치했던 선수의 등수 +1
        players[idx-1], players[idx] = players[idx], players[idx-1] # 위치 변경
    return players