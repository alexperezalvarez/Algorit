from config.wsgi import *
from core.erp.models import Type
def main():
  # Listar

  #select * from Tabla
  #query = Type.objects.all()
  #rint(query)

  #Insercion
  #t = Type()
  #t.name = 'Nuevo Tipo'
  #t.save()

  #edicion
#  try:
 #     t = Type.objects.get(id=1)
#    t.name = 'Tipo Editado'
#      t.save()
#      print(t.name)
#  except Exception as e:
#      print(e)


  #Eliminacion
  #t = Type.objects.get(id=1)
  #t.delete()

 #obj = Type.objects.filter(name__icontains='terry')
 obj = Type.objects.filter(name__startswith='pre')
 print(obj)