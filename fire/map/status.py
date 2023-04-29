from .models import *
from .views import *




def result(idnode):
    nod = node.objects.get(Idnode=idnode)
    print('....node.....',nod)
    fwi = nod.FWI
    print('fff.........fwi',fwi)

    # my_project = myProject.objects.get(polygon_id=id)
    # nodee = node.objects.filter(polyg=my_project).order_by('-Idnode')
    # onode=nodee[0]
    # print('....last.....nodee',onode)
   
    # #node = polygon.node
    # fwi = onode.FWI
    # print('fff....last.....fwi',fwi)

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
    print('sss.........status',status)
    
    

    return status



    # post = Data.objects.order_by('-IdData').first()
    # tempp = post.temperature
    # humm = post.humidity
    # windd = post.wind
    
    # if tempp > 10 and humm < 50 and windd > 0:
    # #if tempp > 20 and humm < 80 and windd > 4:
    #     status = 'Risk'
    # else:
    #     status = 'SAFE'