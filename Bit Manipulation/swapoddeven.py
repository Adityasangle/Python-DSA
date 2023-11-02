def swapBits(n):
        #Your code here
        #
        mod_even = (n<<1)&(0xaaaaaaaa)
        mod_odd= (n>>1)&(0x55555555)
        return mod_even+mod_odd

print(swapBits(23))

# #0xAAAAAAAA is a hexadecimal number that represents a 32-bit integer with all its even bits set to 1 (binary 1010). In other words, it has '1's in positions 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, and 30, where bit positions are counted starting from 0 for the least significant bit.
# When you apply the & operator between N and 0xAAAAAAAA, it effectively "masks" the odd-numbered bits of N with zeros while keeping the even-numbered bits unchanged. This is because the 0xAAAAAAAA number has '1's in all even positions and '0's in all odd positions.
#  the result stored in the even_bits variable will have the same value as N, but with all the odd-numbered bits (bit positions 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, and 31) set to 0, effectively extracting all the even bits from N.
# Let's say N is 0b11011010. (In decimal, this is 218)

# N in binary: 11011010
# 0xAAAAAAAA in binary: 10101010101010101010101010101010
# Now, when you perform N & 0xAAAAAAAA:

# Result in binary: 10001000101000001000100010000000
# Result in decimal: 136848384
# So, even_bits will be 136848384, which is the original value of N with all the odd bits set to 0.

# 0x55555555 is a hexadecimal number that represents a 32-bit integer with all its odd bits set to 1 (binary 0101). In other words, it has '1's in positions 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, and 31, where bit positions are counted starting from 0 for the least significant bit.
# When you apply the & operator between N and 0x55555555, it effectively "masks" the even-numbered bits of N with zeros while keeping the odd-numbered bits unchanged. This is because the 0x55555555 number has '1's in all odd positions and '0's in all even positions.

# So, the result stored in the odd_bits variable will have the same value as N, but with all the even-numbered bits (bit positions 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, and 30) set to 0, effectively extracting all the odd bits from N.

# Let's say N is 0b11011010. (In decimal, this is 218)

# N in binary: 11011010
# 0x55555555 in binary: 01010101010101010101010101010101
# Now, when you perform N & 0x55555555:

# Result in binary: 01010000000000000001000000000000
# Result in decimal: 131072
# So, odd_bits will be 131072, which is the original value of N with all the even bits set to 0.