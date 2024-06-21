def parametros_aplicacion(request):
    titulo_pagina = "DJANGO ISI APP"
    subtitulo_pagina = "Pedidos en Línea"
    
    return {"titulo_principal": titulo_pagina, "subtitulo": subtitulo_pagina}


def valores_carrito(request):
    carrito = request.session.get("carrito_pedido", [])
    cantidad_items = len(carrito)
    total = 0.00
    for item in carrito:
        total = total + item["subtotal"]
        
    return {"carrito_pedido": carrito, "cantidad_items": cantidad_items, "total_carrito": total}