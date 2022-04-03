N = input()
i = 0

if int(N) < 10:
    N = N + '0'

N_new = N

while True:
    N_new = N_new[1] + str(int(N_new[0]) + int(N_new[1]))[-1]
    i += 1

    if N_new == N:
        print(i)
        break