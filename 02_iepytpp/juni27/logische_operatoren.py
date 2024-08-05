def print_expr_result(expr, **kwargs):
    """
    Ich drucke das Ergebnis eines Ausdrucks mit angegebenen Parametern.
    """

    result = eval(expr, {}, kwargs)

    if kwargs:
        print(f"{expr} wobei {kwargs} ist {result}.\n")
    else:
        print(f"{expr} ist {result}.\n")


# ------------------------------------------------


# Evaluieren Sie das Ergebnis der folgenden logischen Ausdrücke:

# (10 > 5) and (-800 > -900)
print_expr_result("(10 > 5) and (-800 > -900)")


#  True and ((100-10) == (-1)*(-95 + 4))
print_expr_result("True and ((100-10) == (-1)*(-95 + 4))")

# False and True
print_expr_result("False and True")

# (True and True) or (False and True)
print_expr_result("(True and True) or (False and True)")

# True and (True or False)
print_expr_result("True and (True or False)")

# True and ((True or False) and True)
print_expr_result("True and ((True or False) and True)")

# x = -10
# ((x + 8) > -2) or (x < -20)
print_expr_result("True and ((True or False) and True)", x=-10)

# x = -10
# ((x + 8) >= -2) or (x < -11)
print_expr_result("((x + 8) >= -2) or (x < -11)", x=-10)

# x = -10
# ((x + 8) >= -2) and (x < -20)
print_expr_result("((x + 8) >= -2) and (x < -20)", x=-10)

# a = 20
# b = 38
# x = 150
# y = 150
# (a != b) and (x != y)
print_expr_result("(a != b) and (x != y)", a=20, b=38, x=150, y=150)

# a = -1
# b = 28
# (a == a) or (a > b)
print_expr_result("(a == a) or (a > b)", a=-1, b=28)

# a = 70
# b = 10
# c = -70
# d = -1
# e = -70
# (a != b) and (c != (d + e))
print_expr_result("(a != b) and (c != (d + e))", a=70, b=10, c=-70, d=-1, e=-70)

# a = 3
# x = -199
# False or ((a*20 + x) > -100) or -1 > 2
print_expr_result("False or ((a*20 + x) > -100) or -1 > 2", a=3, x=-199)
