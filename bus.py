# -*- coding: utf-8 -*-

# Ponto de onibus
# Recebe uma lista ou tupl do tipo : [[10,0],[3,5],[5,8]])

# O objetivo é definir quantas pessoas permanecem após o final

# garatinr que sempre há quantidade de pessoa > 0
# ( IN , OUT )
    def number(bus_stops):
        total = 0
        for stop in bus_stops:
            pin = stop[0]
            pout = stop[1]
            if (total - pout) >= 0:
                total = total - pout + pin
            else: 
                total = total + pin
        return total

#main 

print(number ([[10,0],[3,5],[5,8]]) )

# Best Pratice

def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])