function solution(n) {
    var answer = 0;
    for(i = n; i >= 2; i--){
        if(i % 2 == 0){
            answer += i
        }
    }
    return answer;
}