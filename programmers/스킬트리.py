# inputs
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

# solution
def solution(skill, skill_trees):
    answer = 0

    for i in range(len(skill_trees)):
        check = []
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                check.append(skill_trees[i][j])
        for j in range(len(check)):
            if check[j] != skill[j]:
                answer -= 1
                break

    answer += len(skill_trees)

    return answer

# run
solution(skill, skill_trees)