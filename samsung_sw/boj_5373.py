import sys
import copy
input = sys.stdin.readline


def rotator(arr, d):
    tmp = [['0','0','0'] for _ in range(3)]
    if d == '+':
        tmp[0][0], tmp[1][0], tmp[2][0] = arr[2][0], arr[2][1], arr[2][2]
        tmp[0][1], tmp[1][1], tmp[2][1] = arr[1][0], arr[1][1], arr[1][2]
        tmp[0][2], tmp[1][2], tmp[2][2] = arr[0][0], arr[0][1], arr[0][2]
    else:
        tmp[0][0], tmp[1][0], tmp[2][0] = arr[0][2], arr[0][1], arr[0][0]
        tmp[0][1], tmp[1][1], tmp[2][1] = arr[1][2], arr[1][1], arr[1][0]
        tmp[0][2], tmp[1][2], tmp[2][2] = arr[2][2], arr[2][1], arr[2][0]
    return tmp


for _ in range(int(input())):
    U = [['w', 'w', 'w'] for _ in range(3)]
    F = [['r', 'r', 'r'] for _ in range(3)]
    L = [['g', 'g', 'g'] for _ in range(3)]
    R = [['b', 'b', 'b'] for _ in range(3)]
    B = [['o', 'o', 'o'] for _ in range(3)]
    D = [['y', 'y', 'y'] for _ in range(3)]
    n = int(input())
    ctrl = list(input().split())
    for command in ctrl:
        if command == 'L-':
            tmp_U = copy.deepcopy(U)
            tmp_B = copy.deepcopy(B)
            tmp_D = copy.deepcopy(D)
            tmp_F = copy.deepcopy(F)

            tmp_U[0][0], tmp_U[1][0], tmp_U[2][0] = F[0][0], F[1][0], F[2][0]
            tmp_B[0][2], tmp_B[1][2], tmp_B[2][2] = U[0][0], U[1][0], U[2][0]
            tmp_D[0][2], tmp_D[1][2], tmp_D[2][2] = B[0][2], B[1][2], B[2][2]
            tmp_F[0][0], tmp_F[1][0], tmp_F[2][0] = D[0][2], D[1][2], D[2][2]

            U = copy.deepcopy(tmp_U)
            B = copy.deepcopy(tmp_B)
            D = copy.deepcopy(tmp_D)
            F = copy.deepcopy(tmp_F)

            rotator(L,'-')

        elif command == 'L+':
            tmp_D = copy.deepcopy(D)
            tmp_B = copy.deepcopy(B)
            tmp_U = copy.deepcopy(U)
            tmp_F = copy.deepcopy(F)

            tmp_D[0][2], tmp_D[1][2], tmp_D[2][2] = F[0][2], F[1][2], F[2][2]
            tmp_B[0][2], tmp_B[1][2], tmp_B[2][2] = D[0][2], D[1][2], D[2][2]
            tmp_U[0][0], tmp_U[1][0], tmp_U[2][0] = B[0][2], B[1][2], B[2][2]
            tmp_F[0][0], tmp_F[1][0], tmp_F[2][0] = U[0][0], D[1][0], D[2][0]

            U = copy.deepcopy(tmp_U)
            B = copy.deepcopy(tmp_B)
            D = copy.deepcopy(tmp_D)
            F = copy.deepcopy(tmp_F)

            rotator(L,'+')

        elif command == 'F-':
            tmp_L = copy.deepcopy(L)
            tmp_B = copy.deepcopy(B)
            tmp_R = copy.deepcopy(R)
            tmp_U = copy.deepcopy(U)

            tmp_L[0][2], tmp_L[1][2], tmp_L[2][2] = U[2]
            tmp_B[2] = L[0][2], L[1][2], L[2][2]
            tmp_R[0][0], tmp_R[1][0], tmp_R[2][0] = B[2]
            tmp_U[2] = R[0][0], R[1][0], R[2][0]

            L = copy.deepcopy(tmp_L)
            B = copy.deepcopy(tmp_B)
            R = copy.deepcopy(tmp_R)
            U = copy.deepcopy(tmp_U)

            rotator(F,'-')

        elif command == 'F+':
            tmp_L = copy.deepcopy(L)
            tmp_B = copy.deepcopy(B)
            tmp_R = copy.deepcopy(R)
            tmp_U = copy.deepcopy(U)

            tmp_L[0][2], tmp_L[1][2], tmp_L[2][2] = B[2]
            tmp_B[2] = R[0][0], R[1][0], R[2][0]
            tmp_R[0][0], tmp_R[1][0], tmp_R[2][0] = U[2]
            tmp_U[2] = L[0][2], L[1][2], L[2][2]

            L = copy.deepcopy(tmp_L)
            B = copy.deepcopy(tmp_B)
            R = copy.deepcopy(tmp_R)
            U = copy.deepcopy(tmp_U)

            rotator(F,'+')

        elif command == 'B-':
            tmp_B = copy.deepcopy(B)
            tmp_L = copy.deepcopy(L)
            tmp_U = copy.deepcopy(U)
            tmp_R = copy.deepcopy(R)

            tmp_B[0] = R[0][2], R[1][2], R[2][2]
            tmp_L[0][0], tmp_L[1][0], tmp_L[2][0] = B[0]
            tmp_U[0] = tmp_L[0][0], tmp_L[1][0], tmp_L[2][0]
            tmp_R[0][2], tmp_R[1][2], tmp_R[2][2] = U[0]

            B = copy.deepcopy(tmp_B)
            L = copy.deepcopy(tmp_L)
            U = copy.deepcopy(tmp_U)
            R = copy.deepcopy(tmp_R)

            rotator(B,'-')

        elif command == 'B+':
            tmp_B = copy.deepcopy(B)
            tmp_L = copy.deepcopy(L)
            tmp_U = copy.deepcopy(U)
            tmp_R = copy.deepcopy(R)

            tmp_R[0][2], tmp_R[1][2], tmp_R[2][2] = B[0]
            tmp_B[0] = L[0][0], L[1][0], L[2][0]
            tmp_L[0][0], tmp_L[1][0], tmp_L[2][0] = U[0]
            tmp_U[0] = R[0][2], R[1][2], R[2][2]

            B = copy.deepcopy(tmp_B)
            L = copy.deepcopy(tmp_L)
            U = copy.deepcopy(tmp_U)
            R = copy.deepcopy(tmp_R)

            rotator(B, '+')

        elif command == 'U-':
            tmp_F = copy.deepcopy(F)
            tmp_R = copy.deepcopy(R)
            tmp_B = copy.deepcopy(B)
            tmp_L = copy.deepcopy(L)

            tmp_F[0] = L[0]
            tmp_R[0] = F[0]
            tmp_B[0] = R[0]
            tmp_L[0] = B[0]

            F = copy.deepcopy(tmp_F)
            R = copy.deepcopy(tmp_R)
            B = copy.deepcopy(tmp_B)
            L = copy.deepcopy(tmp_L)

            rotator(U, '-')

        elif command == 'U+':
            tmp_F = copy.deepcopy(F)
            tmp_R = copy.deepcopy(R)
            tmp_B = copy.deepcopy(B)
            tmp_L = copy.deepcopy(L)

            tmp_B[0] = L[0]
            tmp_R[0] = B[0]
            tmp_F[0] = R[0]
            tmp_L[0] = F[0]

            F = copy.deepcopy(tmp_F)
            R = copy.deepcopy(tmp_R)
            B = copy.deepcopy(tmp_B)
            L = copy.deepcopy(tmp_L)

            rotator(U, '+')

        elif command == 'R-':
            tmp_D = copy.deepcopy(D)
            tmp_B = copy.deepcopy(B)
            tmp_U = copy.deepcopy(U)
            tmp_F = copy.deepcopy(F)

            tmp_D[0][0], tmp_D[1][0], tmp_D[2][0] = F[0][2], F[1][2], F[2][2]
            tmp_B[0][0], tmp_B[1][0], tmp_B[2][0] = D[0][0], D[1][0], D[2][0]
            tmp_U[0][2], tmp_U[1][2], tmp_U[2][2] = B[0][0], B[1][0], B[2][0]
            tmp_F[0][2], tmp_F[1][2], tmp_F[2][2] = U[0][2], U[1][2], U[2][2]

            D = copy.deepcopy(tmp_D)
            B = copy.deepcopy(tmp_B)
            U = copy.deepcopy(tmp_U)
            F = copy.deepcopy(tmp_F)

            rotator(R, '-')

        elif command == 'R+':
            tmp_D = copy.deepcopy(D)
            tmp_B = copy.deepcopy(B)
            tmp_U = copy.deepcopy(U)
            tmp_F = copy.deepcopy(F)

            tmp_U[0][2], tmp_U[1][2], tmp_U[2][2] = F[0][2], F[1][2], F[2][2]
            tmp_B[0][0], tmp_B[1][0], tmp_B[2][0] = U[0][2], U[1][2], U[2][2]
            tmp_D[0][0], tmp_D[1][0], tmp_D[2][0] = B[0][0], B[1][0], B[2][0]
            tmp_F[0][2], tmp_F[1][2], tmp_F[2][2] = D[0][0], D[1][0], D[2][0]

            D = copy.deepcopy(tmp_D)
            B = copy.deepcopy(tmp_B)
            U = copy.deepcopy(tmp_U)
            F = copy.deepcopy(tmp_F)

            rotator(R, '+')

        elif command == 'D-':
            tmp_B = copy.deepcopy(B)
            tmp_R = copy.deepcopy(R)
            tmp_F = copy.deepcopy(F)
            tmp_L = copy.deepcopy(L)

            tmp_B[2] = L[2]
            tmp_R[2] = B[2]
            tmp_F[2] = R[2]
            tmp_L[2] = F[2]

            B = copy.deepcopy(tmp_B)
            R = copy.deepcopy(tmp_R)
            F = copy.deepcopy(tmp_F)
            L = copy.deepcopy(tmp_L)

            rotator(D, '-')

        elif command == 'D+':
            tmp_B = copy.deepcopy(B)
            tmp_R = copy.deepcopy(R)
            tmp_F = copy.deepcopy(F)
            tmp_L = copy.deepcopy(L)

            tmp_L[2] = B[2]
            tmp_B[2] = R[2]
            tmp_R[2] = F[2]
            tmp_F[2] = L[2]

            B = copy.deepcopy(tmp_B)
            R = copy.deepcopy(tmp_R)
            F = copy.deepcopy(tmp_F)
            L = copy.deepcopy(tmp_L)

            rotator(D, '+')

    print(*U, sep='\n')

