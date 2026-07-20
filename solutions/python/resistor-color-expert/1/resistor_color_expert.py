COLORS = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]

TOLERANCES = {
'grey': '0.05%',
'violet': '0.1%',
'blue': '0.25%',
'green': '0.5%',
'brown': '1%',
'red': '2%',
'gold': '5%',
'silver': '10%'
}

def resistor_label(colors):
    if len(colors) == 1:
        return '0 ohms'
    if len(colors) == 4:
        col1, col2, mult, tol = colors
        col3 = None
    else:
        col1, col2, col3, mult, tol = colors

    val1 = COLORS.index(col1)
    val2 = COLORS.index(col2)
    if col3:
        val3 = COLORS.index(col3)
    else:
        val3 = ''

    big_val = int(str(val1) + str(val2) + str(val3)) * 10**COLORS.index(mult)

    if big_val >= 1_000_000_000:
        prefix = 'giga'
        big_val /= 1_000_000_000
    elif big_val >= 1_000_000:
        prefix = 'mega'
        big_val /= 1_000_000
    elif big_val >= 1_000:
        prefix = 'kilo'
        big_val /= 1_000
    else:
        prefix = ''

    tolerance = TOLERANCES[tol]
    big_val = str(big_val)
    if big_val.endswith('.0'):
        big_val = big_val.strip('.0')

    return f'{big_val} {prefix}ohms ±{tolerance}'