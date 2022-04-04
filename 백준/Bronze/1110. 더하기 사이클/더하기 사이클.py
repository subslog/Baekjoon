N = N_new = int(input())
i = 0

while True:
    N_post = N_new // 10
    N_end = N_new % 10
    N_new = (N_end * 10) + ((N_post + N_end) % 10)
    i += 1

    if N_new == N:
        print(i)
        break