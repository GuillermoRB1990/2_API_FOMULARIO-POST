@app.post("/agregar")
async def agregar(request:Request):
    datos = await cargarJSON()
    nuevos_datos = {}
    datos_formulario = await request.form()
    #print(len(datos))
    #print(datos)
    #print("fin de prueba")
    ultmimo_id = datos[-1].get("item_id")  #valor del ide del ultimo elemento de la lista
    #print(datos_formulario)
    #print(datos_formulario["f_nombre"])
    #print(datos_formulario.items)
    nuevos_datos["item_id"] = ultmimo_id+1
    nuevos_datos["matricula"] = int(datos_formulario["f_matricula"])
    nuevos_datos["nombre"] = datos_formulario["f_nombre"]
    nuevos_datos["apaterno"] = (datos_formulario["f_apaterno"])
    nuevos_datos["amaterno"] = (datos_formulario["f_amaterno"])
    nuevos_datos["edad"] = int(datos_formulario["f_edad"])
    nuevos_datos["correo"] = (datos_formulario["f_correo"])
    nuevos_datos["telefono"] = int(datos_formulario["f_telefono"])
    nuevos_datos["carrera"] = (datos_formulario["f_carrera"])
    print(nuevos_datos)
    datos.append(nuevos_datos)
    print(datos)

    await guardarJSON(datos)

    return RedirectResponse("/lista",303)