import sys
from .bring import find_content

def main():
    args = sys.argv[1:]
    find_content(' '.join(map(str, args)) )

if __name__ == '__main__':
    main()