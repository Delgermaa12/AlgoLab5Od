import sys
def solve():
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        depths = [0] * n

        def build(l, r, depth):
            if l > r:
                return
            mx = a[l]
            pos = l
            for i in range(l, r + 1):
                if a[i] > mx:
                    mx = a[i]
                    pos = i
            depth[pos] = depth
            build(l, pos - 1, depth + 1)
            build(pos + 1, r, depth + 1)

        build(0, n - 1, 0)
        print("".join(map(str, depths)))


if __name__ == "__main__":
    solve()
