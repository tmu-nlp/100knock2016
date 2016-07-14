from collections import defaultdict
from knock83 import getFreq
import math


def getPPMI():
  coocurrence, tokens, context, N = getFreq()
  PPMI = defaultdict(lambda: defaultdict(lambda: 0.0))
  for t, contexts in coocurrence.items():
    for c, count in contexts.items():
      if count >= 10:
        PPMI[t][c] = max(math.log((N * count) / (tokens[t] * context[c]), 2), 0)
  return PPMI

def main():
  ppmi = getPPMI()
  print(ppmi)

if __name__ == '__main__':
  main()
