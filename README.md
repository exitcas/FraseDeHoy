# #FraseDeHoy
Bot que uso a veces en mi cuenta de Mastodon para subir frases de mi [base de datos de frases](https://frases.atico.ga) usando el hashtag [#FraseDeHoy](https://koyu.space/web/tags/FraseDeHoy).

## Instalar
1. Instalar los requerimientos ([`Mastodon.py`](https://pypi.org/project/Mastodon.py/) y [`frases`](https://pypi.org/project/frases/)).
    - Via PIP: `pip install -r requirements.txt`
    - Via Poetry: `poetry lock&&poetry install`
    - Via Pipenv: `pipenv install -r requirements.txt`
    - **[NOTA]** Si usted quiere usar una base de datos independiente, en vez de instalar Frases.py, puede editar su código fuente y luego instalarlo con PIP, o puede directamente instalar [`requests`](https://pypi.org/project/requests/), luego descargar y editar la última versión del archivo "[`__init__.py`](https://github.com/Luqaska/frases.py/blob/main/frases/__init__.py)" y luego renombrarlo a "`frases.py`".
2. Crear una aplicación en el portal de desarrollo de tu instancia de Mastodon.
3. Colocarle los scopes `write` y `write:statuses`.
4. Crear un archivo de con el token de acceso de tu aplicación.
5. Editar las primeras lineas de "`mf.py`".
6. Ejecutar "`mf.py`" cada vez que se quiera subir una frase.
