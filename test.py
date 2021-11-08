new_id = "=.="
answer = ""

#1단계
new_id = new_id.lower()
print(new_id)
    
#2단계
for word in new_id:
    if word.isalnum() or word in '-_.':
        answer += word
print(answer)            
#3단계
while '..' in answer:
    answer = answer.replace('..', '.')
print(answer)        
#4단계
answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
answer = answer[:-1] if answer[-1] == '.' else answer
print(answer)
#5단계
if len(answer) == 0:
    answer = 'a'
print(answer)        
#6단계
if len(answer) >= 16:
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
print(answer)   
#7단계
if len(answer) <= 3:
    answer = answer + answer[-1] * (3-len(answer))

print(answer)