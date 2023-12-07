from collections import Counter
from dataclasses import dataclass, field
from functools import total_ordering


LABELS = (
    'J',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'T',
    'Q',
    'K',
    'A'
)

HAND_TYPES = (
    'high',
    'one',
    'two',
    'three',
    'full_house',
    'four',
    'five'
)


@dataclass
@total_ordering
class Hand:
    hand_type: int = field(init=False)
    cards: str
    bid: int

    def __post_init__(self):
        self.hand_type = HAND_TYPES.index(self._determine_hand_type())

    def __lt__(self, other):
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        else:
            for i in range(len(self.cards)):
                if self.cards[i] != other.cards[i]:
                    self_index = LABELS.index(self.cards[i])
                    other_index = LABELS.index(other.cards[i])
                    return self_index < other_index


    def _determine_hand_type(self):
        hand = self.cards
        hand_type = HAND_TYPES[0]

        counter = Counter(hand)
        counts = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        if len(counts) > 1:
            high_count = counts[0][1] + counter.get('J', 0) if counts[0][0] != 'J' else counts[1][1] + counts[0][1]
        else:
            high_count = counts[0][1]
        
        if len(counts) > 2:
            penult_count = counts[1][1] if counts[0][0] != 'J' else counts[2][1]
        else:
            penult_count = counts[1][1] if counts[0][0] != 'J' else 0

        if high_count == 5:
            hand_type = HAND_TYPES[6]
        elif high_count == 4:
            hand_type = HAND_TYPES[5]
        elif high_count == 3 and penult_count == 2:
            hand_type = HAND_TYPES[4]
        elif high_count == 3:
            hand_type = HAND_TYPES[3]
        elif high_count == 2 and penult_count == 2:
            hand_type = HAND_TYPES[2]
        elif high_count == 2:
            hand_type = HAND_TYPES[1]
        
        return hand_type


def solution(lines):
    hands = []
    total = 0
    for line in lines:
        cards, bid = line.split()
        hands.append(Hand(cards, int(bid)))

    for i, hand in enumerate(sorted(hands), start=1):
        total += hand.bid * i

    return total


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))
