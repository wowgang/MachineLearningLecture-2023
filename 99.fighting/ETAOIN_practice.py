"""Map letters from string into dictionary & print bar chart of frequency."""
"""문자열의 문자를 사전으로 매핑하고 빈도 막대 차트를 인쇄합니다."""
import sys
import pprint
from collections import defaultdict

# Note: text should be a short phrase for bars to fit in IDLE window
# 참고: IDLE 창에 맞도록 텍스트는 짧은 문구여야 합니다.
text = 'Like the castle in its corner in a medieval game, I foresee terrible \
trouble and I stay here just the same.'

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# defaultdict module lets you build dictionary keys on the fly!
# defaultdict 모듈을 사용하면 즉시 사전 키를 빌드할 수 있습니다!
mapped = defaultdict(list)
for character in text:
    character = character.lower()
    if character in ALPHABET:
        mapped[character].append(character)

# pprint lets you print stacked output
# pprint를 사용하면 쌓인 출력물을 인쇄할 수 있습니다.
print("\nYou may need to stretch console window if text wrapping occurs.\n")
print("text = ", end='')
print("{}\n".format(text), file=sys.stderr)
pprint.pprint(mapped, width=110)
