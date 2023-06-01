from .models import *
from .views import *




def result(idnode):
    nod = node.objects.get(Idnode=idnode)
    fwi = nod.FWI

    if fwi is not None and 0 <= fwi <= 7:
        status = 'DOWN'
    elif fwi is not None and 8 <= fwi <= 16:
        status = 'MODERATE'
    elif fwi is not None and 17 <= fwi <= 25:
        status = 'HIGH'
    elif fwi is not None and 26 <= fwi <= 31:
        status = 'VERY HIGH'
    elif fwi is not None and fwi > 31:
        status = 'EXTREME' 
    else:
        status = 'UNKNOWN'

    return status
