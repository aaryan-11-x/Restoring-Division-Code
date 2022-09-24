from collections import deque


# Function Which Calculates 2's Compliment
def comp_2(div):
    k = 0
    comp2 = div
    for n in reversed(range(len(comp2))):
        if comp2[n] == '1':
            k = n
            break
    for n in reversed(range(k)):
        if comp2[n] == '0':
            comp2[n] = '1'
        elif comp2[n] == '1':
            comp2[n] = '0'
    comp2 = [str(u) for u in comp2]
    return comp2


Q = list(bin(int(input("Enter The Dividend : "))).replace('0b', '0'))
M = bin(int(input("Enter The Divisor : "))).replace('0b', '0')
M_temp = list(M)
M = list(M)
A, whole = [], []

# Making The Binary Values Of Equal Length
if len(Q) < len(M):
    while len(Q) != len(M):
        Q.insert(0, '0')
if len(M) < len(Q):
    while len(Q) != len(M):
        M.insert(0, '0')
while len(A) != len(M):
    A.append('0')
M_temp = M

M_Comp2 = (comp_2(M_temp))
M_Comp2 = ''.join(M_Comp2)
for i in A:
    whole.append(i)
for i in Q:
    whole.append(i)
whole = deque(whole)  # 'Whole' Contains Bits Of A & Q Combined

print('_' * 50)
print("A\t\tQ\t\tOperation")
print('_' * 50)

op1, op3 = "Left Shift", 'Unsuccessful (Restoration)'
print(f"{''.join(A)}\t{''.join(Q)}")
print('_' * 50)

# Algorithm Implementation
for i in range(len(Q)):
    whole.rotate(-1)  # Left Shifts The Bits
    A, Q = list(whole), list(whole)
    A, Q = A[:len(M)], Q[len(M):]
    Q[len(M) - 1] = '_'  # Deletes The Q0 Bit
    A, Q = ''.join(A), ''.join(Q)
    print(f"{A}\t{Q}\t{op1}")
    A_temp = A
    A = str(bin(int(A, 2) + int(M_Comp2, 2))).replace('0b', '')     # A = A - M
    if len(A) > len(M):
        A = A[1:]       # Deletes The Carry
    A_temp2 = A
    Q = list(Q)
    # Condition For Unsuccessful
    if A[0] == '1':
        Q[len(M) - 1] = '0'
        A = A_temp      # A = A + M (Restoration)
    # Condition For Successful
    elif A[0] == '0':
        Q[len(M) - 1] = '1'
        for x in range(len(M)):
            whole[x] = A[x]
        for x in range(len(M)):
            whole[x + len(M)] = Q[x]
    op2 = f"A <- A - M; Q\u2080 <- {Q[len(M) - 1]}"
    Q = ''.join(Q)
    print(f"{A_temp2}\t{Q}\t{op2}")
    if A_temp2[0] == '1':
        print(f"{A}\t{Q}\t{op3}")
    print('_' * 50)

print(f"Remainder = {int(A, 2)}")
print(f"Quotient = {int(Q, 2)}")
