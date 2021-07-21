# 문자열 내 p와 y의 개수

```python
def solution(s):
    answer = True
    pcnt, ycnt = 0, 0
    
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            pcnt += 1
        elif s[i] == 'y' or s[i] == 'Y':
            ycnt += 1
    
    if pcnt != ycnt:
        answer = False

    return answer
```

