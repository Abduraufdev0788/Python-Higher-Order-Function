sentence = "Functional programming in Python is very powerful and elegant"

text = sentence.split()

lens = list(sorted(text, key=lambda x : len(x), reverse=False))
print(lens[-3:])