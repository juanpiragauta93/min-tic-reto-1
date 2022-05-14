
def solucion():

    masproductos="s"
    total=0
    while masproductos=="s" or masproductos=="S":

        valorUnitario=float(input("valor unitario del producto-> "))
        tieneIva=input("¿el producto cuenta con IVA? S/N-> ")
        cantidadproducto=float(input("Cantidad del Producto-> "))
        if tieneIva=="s" or tieneIva=="S":
            print("IVA incluído")
            subtotal=(valorUnitario+valorUnitario*0.19)*cantidadproducto
            total=subtotal+total
            print("SUBTORAL-> ")
            print(total)
            
        elif tieneIva=="n" or tieneIva=="N":
            print ("Producto sin IVA")
            subtotal=valorUnitario*cantidadproducto
            total=subtotal+total
            print("SUBTORAL-> ")
            print(total)
            
        masproductos=input("Faltan productos por cobrar?-> ")
    
    print("TOTAL A COBRAR: ",total)



      
    
        

        


        

    
    
  










solucion()




