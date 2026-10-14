# Match de Mesa — versión móvil

Aplicación web en Python con Streamlit, adaptada a pantallas pequeñas de iPhone (Safari) y Android (Chrome).

## Publicarla para usarla desde el móvil
1. Descomprime el ZIP.
2. Sube `app.py` y `requirements.txt` a un repositorio de GitHub.
3. Abre https://share.streamlit.io/ e inicia sesión con GitHub.
4. Pulsa **Create app**, elige el repositorio y `app.py`, y publícala.
5. Abre la URL que te proporcione Streamlit desde Safari en iPhone o Chrome en Android. Puedes compartir esa misma URL con tu pareja.

No hay que instalar nada. Si queréis, podéis añadir la página a la pantalla de inicio desde el menú Compartir de Safari (iPhone) o el menú de Chrome (Android); seguirá siendo una web.

## Ejecutar en local
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Alcance
Esta versión está optimizada para móvil y se usa por turnos en un mismo teléfono. La sesión mantiene los votos mientras la app siga activa, pero todavía no sincroniza votos entre dos teléfonos distintos ni almacena resultados de forma permanente.
