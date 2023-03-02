    habitantes_ultima_ciudad = 0
    for ciudad in lista_ciudades:
       
        if ciudad['habitantes'] < habitantes_ultima_ciudad:
            continue
        else:
            print(ciudad['habitantes'])    
        habitantes_ultima_ciudad = ciudad['habitantes']
