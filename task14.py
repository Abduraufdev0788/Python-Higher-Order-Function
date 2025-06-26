words = ["sun", "mountain", "a", "apple"]

lens_Sorts = list(sorted(words, key=lambda x : len(x), reverse=True))

print(lens_Sorts)