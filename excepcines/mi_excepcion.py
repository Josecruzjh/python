#creando mi primera esepcion persona
class MiExcepcion(Exception):
    def __init__(self,err):
       print(f"Imprecionante,cometiste el sigiente error: {err}")
       
       #lanzando mi primeraesepcion
    #raise MiExcepcion("jajajajajajajaj,persona oculta")
    
    
       # manejandola
try:
    raise MiExcepcion("jajajajajajajaj,persona oculta")
except:
    print("como vas a cometer ese error?")
    