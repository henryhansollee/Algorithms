# 코딩테스트 고득점 Kit

## 1. 해시

### 1-1. 완주하지 못한 선수

```python
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    answer = participant[-1]
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer
```



### 1-2. 전화번호 목록

```python
def solution(phone_book):
    answer = True
    n = len(phone_book)
    phone_book.sort()
    for i in range(n-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
    return answer
```



### 1-3. 위장

```python
def solution(clothes):
    answer = 1
    
    dict_clothes = {}
    for i in range(len(clothes)):
        key = clothes[i][1]
        val = clothes[i][0]
        if key in dict_clothes:
            dict_clothes[key].append(val)
        else:
            dict_clothes[key] = [val]
    
    for key in dict_clothes.keys():
        answer = answer * (len(dict_clothes[key]) + 1)

    return answer - 1
```



### 1-4. 베스트앨범

```python

```



## 2. 정렬

### 2-1. K번째수

```python
def solution(array, commands):
    answer = []
    for command in commands:
        sliced_array = array[command[0]-1:command[1]]
        sliced_array.sort()
        answer.append(sliced_array[command[2]-1])
    return answer
```



### 2-2. 가장 큰 수

```python

```



### 2-3. 

```python

```

