from collections import defaultdict


def getFreq():
  coocurrence = defaultdict(lambda: defaultdict(lambda: 0))
  token = defaultdict(lambda: 0)
  context = defaultdict(lambda: 0)
  N = 0
  for line in open('./token-context.txt', 'r'):
    tokens = line.strip('\n').split('\t')
    coocurrence[tokens[0]][tokens[1]] += 1
    token[tokens[0]] += 1
    context[tokens[1]] += 1
    N += 1
  return coocurrence, token, context, N

def main():
  coo, tok, con, n = getFreq()
  for token, contexts in coo.items():
    for context, count in contexts.items():
      print("{}, {}:\t{}".format(token, context, count))

  for token, count in tok.items():
    print("{}, *:\t{}".format(token, count))

  for context, count in con.items():
    print("*, {}:\t{}".format(context, count))

  print("N:\t{}".format(n)) 
if __name__ == '__main__':
    main()
