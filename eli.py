from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def mostrar_inicio():
    contenido_html="""
    <html>
        <head>
            <title>Equipo2</title>
        </head>
        <body>
            <h3> Bienvenidos</h3>
            <p>Este sitio pertence al Equipo2 y mostrará los datos de los integrantes</p>
            <ul>
                <li>Guillermo</li>
                <li>Rodan Alberto</li>
                <li>Eleazar</li>
                <li>Daniel Antorio</li>
                <li>Luis Alan</li>
            </ul>
            <a href="equipo2.html"> Equipo2</a>
    </body>
    </html>
    """
    return HTMLResponse(content=contenido_html, status_code=200)