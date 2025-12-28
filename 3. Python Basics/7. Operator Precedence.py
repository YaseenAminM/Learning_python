# ##############################
# Operator Precedence

print(20 - 3 * 4)
print((20 - 3) * 4)
print((20 - 3) * 4 ** 2)


# Order
# 1. ()                     Parentheses
# 2. **                     Exponentiation
# 3. +x  -x  ~x             Unary plus, minus, bitwise NOT
# 4. *  /  //  %            Multiplication, Division, Floor division, Modulus
# 5. +  -                   Addition, Subtraction
# 6. <<  >>                 Bitwise shifts
# 7. &                      Bitwise AND
# 8. ^                      Bitwise XOR
# 9. |                      Bitwise OR
# 10. == != > < >= <=       Comparisons
# 11. not                   Logical NOT
# 12. and                   Logical AND
# 13. or                    Logical OR
