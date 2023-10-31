n = int(input())  # Number of genome fragments
fragments = [input() for _ in range(n)]

fragments = [fragment for fragment in fragments if not fragment.isdigit()]
fragment_characters = [[char for char in fragment] for fragment in fragments] // chars

print (fragment_characters)

