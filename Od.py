import sys

def solve():
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        depths = [0] * n

        def build(l, r, d):
            if l > r:
                return

            mx = a[l]
            pos = l
            for i in range(l, r + 1):
                if a[i] > mx:
                    mx = a[i]
                    pos = i

            depths[pos] = d
            build(l, pos - 1, d + 1)
            build(pos + 1, r, d + 1)

        build(0, n - 1, 0)
        print("".join(map(str, depths)))


if __name__ == "__main__":
    solve()
