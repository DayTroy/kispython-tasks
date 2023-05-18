def main(whole):
    mask_k1 = 0b000000000000000000001111
    mask_k2 = 0b000000000000000000110000
    mask_k3 = 0b000000000000011111000000
    mask_k4 = 0b111111111111100000000000
    k1 = (whole & mask_k1)
    k2 = (whole & mask_k2) >> 4
    k3 = (whole & mask_k3) >> 6
    k4 = (whole & mask_k4) >> 11
    return [('K1', k1), ('K2', k2), ('K3', k3), ('K4', k4)]


print(main(299830))
print(main(552109))
print(main(889299))
print(main(450125))