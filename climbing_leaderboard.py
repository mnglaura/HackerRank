alice_score = [50, 65, 77, 90, 102]
scores = [100, 90, 90, 80, 75, 60]

def climbingLeaderboard(scores, alice):
    rank_list = []
    for score in alice_score:
        rank = count_rank(scores, score)
        rank_list.append(rank)
    return rank_list

def count_rank(scores, alice_score):
    index = -1

    for i in range(0, len(scores)):
        if alice_score <= scores[i]:
            continue
        else:
            index = i
            break

    if index == -1:
        index = len(scores)

    scores.insert(index, alice_score)
 
    rank = 1

    for i in range(1, index+1):
        if scores[i] < scores[i-1]:
            rank += 1

    return rank
    
print(climbingLeaderboard(scores, alice_score))