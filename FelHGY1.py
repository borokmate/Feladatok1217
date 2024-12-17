"""
Készítsen programot, amely bekér 5 mondatot, majd kiírja a legtöbb szóközt tartalmazó mondatot!
"""

sentences = [input("Adjon meg big sentencet: ") for i in range(5)]

sent_len = [len(i.split(" ")) for i in sentences]

max_len = 0
longest_index = 0

for i in range(len(sent_len)):
    if sent_len[i] > max_len:
        max_len = sent_len[i]
        longest_index = i

print(sentences[longest_index])