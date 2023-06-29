"""Turn a word into its Pig Latin equivalent."""
"""단어를 돼지 라틴어로 변환."""
import sys

VOWELS = 'aeiouy'

while True:
    # 단어를 입력하고 돼지 라틴어 번역을 받으세요:
    # word = input("Type a word and get its pig Latin translation: ")
    word = input("단어를 입력하고 돼지 라틴어 번역을 받으세요: ")


    if word[0] in VOWELS:
        pig_Latin = word + 'way'
    else:
        pig_Latin = word[1:] + word[0] + 'ay'
    print()
    print("{}".format(pig_Latin), file=sys.stderr)

    # 다시 시도하십시오? (종료하려면 Enter else n을 누르십시오.)
    # try_again = input("\n\nTry again? (Press Enter else n to stop)\n ")
    try_again = input("\n\n다시 시도할래? (종료하려면 Enter else n을 누르십시오.)\n ")
    if try_again.lower() == "n":
        sys.exit()
