import hashlib as h
from random import randint

def id_creator(date):
    """
Creates the id of any object by using its creation date in format
YYYYmmDDHHMMSS and 5 magic numbers. For one date, there are
approximatively 2.5 * 10**12 possible combinations, should be
enough for a long long time.
    """
    m1=randint(150,300)
    m2=randint(0,100)
    m3=randint(2400,6000)
    m4=randint(0,40)
    m5=randint(1,1000)
    sm=m1*(10**10)-m2*(10**6)+m3*(10**2)+m4
    code=(date+sm)*m5
    code_bytes=code.to_bytes(16,'big')
    db_id = h.sha1()
    db_id.update(code_bytes)
    return db_id.hexdigest() 

# print(id_creator(20250701104150))
