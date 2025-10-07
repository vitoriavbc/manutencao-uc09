# ==========================================================
# 🧩 ATIVIDADE 7 - Versionamento com Git
# Códigos CORRIGIDOS
# ==========================================================

# 1️⃣ Desafio 1
def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

a = 10
b = 0
resultado = dividir(a, b)
print(f"O resultado da divisão é: {resultado}")

# 2️⃣ Desafio 2
nome_usuario = "Professor(a)"
print("Olá, " + nome_usuario)

# 3️⃣ Desafio 3
frutas = ["maçã", "banana", "laranja"]
print(f"Minhas frutas favoritas: {frutas}")

# 4️⃣ Desafio 4 - HTML
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Bug de Tag</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1 class="titulo">Página com Bug de Estrutura</h1>
    <p>Este é o primeiro parágrafo.</p>
    <div id="status">Verificando JS...</div>
    <script src="script.js"></script>
</body>
</html>
"""

# 5️⃣ Desafio 5 - CSS
css = """
.titulo {
    font-size: 24px;
    color: blue;
    background-color: yellow;
    padding: 10px;
    border: 1px solid black;
}
"""

# 6️⃣ Desafio 6 - JavaScript
js = """
let valor = 5;
let elemento = document.getElementById("status");

if (valor == 10) {
    elemento.innerText = "A condição é sempre verdadeira! (Bug corrigido)";
} else {
    elemento.innerText = "A condição é falsa.";
}
"""

# 7️⃣ Desafio 7 - Django
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("Olá do Django!")

# 8️⃣ Desafio 8 - Django
from django.urls import path
from django.http import HttpResponse
from . import views

def outra_view(request):
    return HttpResponse("Outra view funcionando!")

urlpatterns = [
    path('ola/', views.saudacao),
    path('outra/', outra_view),
]

# 9️⃣ Desafio 9 - Kivy
from kivy.app import App
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        return Label(text='Kivy App com Bug Corrigido')

MinhaApp().run()

# 🔟 Desafio 10 - Kivy
from kivy.app import App
from kivy.uix.button import Button

class OutraApp(App):
    def build(self):
        return Button(text='Corrija o Retorno!')

OutraApp().run()
