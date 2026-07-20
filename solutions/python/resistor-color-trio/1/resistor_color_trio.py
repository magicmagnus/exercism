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

PREFIX = {
    3: 'kilo',
    6: 'mega',
    9: 'giga'
}

def label(colors):
    first_two = str(COLORS.index(colors[0])) + str(COLORS.index(colors[1]))

    res = int(first_two) * 10**COLORS.index(colors[2])

    pre = ''
    new_res = res
    
    for fac, prefix in PREFIX.items():
        if res / 10**fac > 1:
            new_res = int(res / (10**fac))
            pre = prefix
            
            

    return str(new_res) + f' {pre}ohms'
    
