def mortgage(principle, interest_rate, year_term, interval_compounding = 'Annually'):
    interval={'a': 1, 'q': 4, 'm': 12, 'd': 365, 'c': 365*24*60}
    
    
    r = (interest_rate/100)/interval[interval_compounding[0].lower()]
    n = year_term * interval[interval_compounding[0].lower()]
    print(r*100,n)
    
    return principle * ( (r*(1+r)**n) / (((1+r)**n)-1) ) 
