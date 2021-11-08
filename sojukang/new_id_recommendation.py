def solution(new_id):
    answer = ''
    word_allowed = ['-', '_']
    # 1단계 
    new_id = new_id.lower()
    
    for i in range(len(new_id)):
        # 2단계 
        if new_id[i] in word_allowed or new_id[i].isalnum():
            answer += new_id[i]

        # 3단계
        if new_id[i] == '.':
            if answer and answer[-1] == '.':
                continue
            else:
                answer += new_id[i]
    
    # 4단계
    if answer and answer[0] == '.':
        answer = answer[1:]

    if answer and answer[-1] == '.':
        answer = answer[:-1]
        
    # 5단계
    if not answer:
        answer = 'a'

    # 6단계
    answer = answer[:15]
    if answer and answer[-1] == '.':
        answer = answer[:-1]

    # 7단계
    while len(answer) < 3:
        if answer:
            answer += answer[-1]

    return answer

solution("=.=")