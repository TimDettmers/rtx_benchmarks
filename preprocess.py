import nltk
with open('./wikitext-2/train_processed.txt', 'w') as g:
    with open('./wikitext-2/train.txt') as f:
        for i, line in enumerate(f):
            if i % 10000 == 0: print(i)
            line = line.strip()
            if len(line) < 100:
                continue

            words = nltk.word_tokenize(line)
            n = len(words)

            g.write(' '.join(words[:n//2]) + '\t' + ' '.join(words[n//2:]) + '\n')
