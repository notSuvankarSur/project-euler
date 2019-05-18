from collections import Counter

hands = list(line.split() for line in open('p054_poker.txt'))
values = {card: value for value, card in enumerate('23456789TJQKA', 2)}
straights = [(t, t - 1, t - 2, t - 3, t - 4) for t in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
ranks = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (), (), (3, 2), (4, 1)]


def hand_rank(hand):
    d = Counter(x[0] for x in hand)
    score = sorted(((v, values[k]) for k, v in d.items()))
    score_tup = [(), ()]
    for item in score:
        score_tup[0] += (item[0],)
        score_tup[1] += (item[1],)
    score_tup[0] = tuple(reversed(score_tup[0]))
    score_tup[1] = tuple(reversed(score_tup[1]))
    score_tup[0] = ranks.index(score_tup[0])
    if len(set(card[1] for card in hand)) == 1:
        score_tup[0] = 5
    if score_tup[1] in straights:
        if score_tup[0] == 5:
            score_tup[0] = 8
        else:
            score_tup[0] = 4
    return score_tup


count = 0
for h in hands:
    if hand_rank(h[:5]) > hand_rank(h[5:]):
        count += 1

print(count)
