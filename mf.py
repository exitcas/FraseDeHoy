from frases import frase
from mastodon import Mastodon

# Iniciar sesión
m = Mastodon(
	# Instancia
	api_base_url = "https://example.com",
	# Ruta del archivo de texto donde se encuentra el token
	access_token = "access_token.txt"
)
f = frase()

# Detectar si el autor es anónimo
if not f['autor']: f['autor'] = "Anónimo"

# Enviar toot
t = m.toot(f"#FraseDeHoy:\n\"{f['frase']}\"\n--{f['autor']}")


# Abrir y verificar la existencia de "logs.txt"
try:
	l = open("logs.txt", "r")
	c = l.read()
	l.close()
except:
	c = False


# Escribir "logs.txt"
l = open("logs.txt", "w+")
w = "\n============================================\n"

if not c:
	c = ""
	w = "LOGS =======================================\n"

t = f"\"{f['frase']}\"\n--{f['autor']}\n\n{t['url']}"
l.write(c + w + t)
l.close()

# Confirmar publicación
print(t)