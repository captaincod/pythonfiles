def logical_xor(a, b):
    if bool(a) == bool(b):
        return False
    else:
        return a or b


G1 = [1 * 10]
G2 = [1 * 10]

G2_taps = {
    1: '2,6', 2: '3,7', 3: '4,8', 4: '5,9',  5: '1,9', 6: '2,10', 7: '1,8', 8: '2,9',
    9: '3,10', 10: '2,3', 11: '3,4', 12: '5,6',  13: '6,7', 14: '7,8', 15: '8,9', 16: '9,10',
    17: '1,4', 18: '2,5', 19: '3,6', 20: '4,7',  21: '5,8', 22: '6,9', 23: '1,3', 24: '4,6',
    25: '5,7', 26: '6,8', 27: '7,9', 28: '8,10',  29: '1,6', 30: '2,7', 31: '3,8', 32: '4,9',
}

file = open('a_lot_of_prn_ids.txt')
# a_lot_of_prn_ids has lines with id's
text = file.read().splitlines()

ca_code = ''

for line in text:
    prn_id = int(line)
    G1.insert(0, logical_xor(G1[2], G1[9]))
    G1.pop()
    first_summand = G1[-1]

    firstG2 = logical_xor(G2[1], G2[2])
    secondG2 = logical_xor(G2[5], G2[7])
    thirdG2 = logical_xor(G2[8], G2[9])
    forthG2 = logical_xor(secondG2, thirdG2)
    G2.insert(0, logical_xor(firstG2, forthG2))
    G2.pop()
    indexes = G2_taps[prn_id].split(',')
    second_summand = logical_xor(G2[int(indexes[0])], G2[int(indexes[1])])

    ca_code += logical_xor(first_summand, second_summand)

file.close()

print(ca_code)
