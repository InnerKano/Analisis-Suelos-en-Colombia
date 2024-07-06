import api 
import ui 
def main():
    ui.Bienvenida()
    print(api.queries(ui.departamento(),ui.municipio(),ui.cultivo(),ui.limite()))
main()
'''
CUNDINAMARCA
FUNZA
Uchuva
10
'''