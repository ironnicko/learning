import sys

sys.stderr.write('test')
sys.stderr.flush()
sys.stdout.write('\nGG\n')


if sys.argv[1]:
    arr = sys.argv[1:]
print(*arr)
