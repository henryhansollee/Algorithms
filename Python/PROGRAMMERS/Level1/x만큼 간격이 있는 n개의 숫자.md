# x만큼 간격이 있는 n개의 숫자

```python
def solution(x, n):
    answer = []
    num = x
    answer.append(num)
    for _ in range(n-1):
        num += x
        answer.append(num)
    return answer
```

