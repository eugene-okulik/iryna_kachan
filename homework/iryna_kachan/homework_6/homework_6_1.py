text = """Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"""
words = text.split()
fin_text = []
for word in words:
    if ',' in word:
        fin_text.append(word.replace(',', 'ing,'))
    elif '.' in word:
        fin_text.append(word.replace('.', 'ing.'))
    else:
        fin_text.append(word + 'ing')
print(' '.join(fin_text))
