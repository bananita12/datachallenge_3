{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b3210a11",
   "metadata": {},
   "outputs": [],
   "source": [
    "class SistemaPlanetario:\n",
    "    def __init__(self, *planetas):\n",
    "        self.estrellas = []\n",
    "        self.planetas = list(planetas)\n",
    "    \n",
    "    def agregar_estrella(self, estrella):\n",
    "        self.estrellas.append(estrella)\n",
    "    \n",
    "    def agregar_planeta(self, planeta):\n",
    "        self.planetas.append(planeta)\n",
    "    \n",
    "    def imprimir_informacion_publica(self):\n",
    "        print(\"Información pública de los sistemas planetarios:\")\n",
    "        for estrella in self.estrellas:\n",
    "            print(f\"Nombre: {estrella.nombre}, Masa: {estrella._masa}, Radio: {estrella._radio}, Temperatura: {estrella._temperatura}, Distancia: {estrella._distancia}, Movimiento propio: {estrella._movimiento_propio}\")\n",
    "        \n",
    "        print(\"Información pública de los planetas:\")\n",
    "        for planeta in self.planetas:\n",
    "            print(f\"Nombre: {planeta.nombre}, Masa: {planeta.masa}, Radio: {planeta.radio}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0faac985",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "import string\n",
    "\n",
    "class Estrella:\n",
    "    def __init__(self, nombre, masa, radio, temperatura, distancia, movimiento_propio):\n",
    "        self.nombre = nombre\n",
    "        self._masa = masa\n",
    "        self._radio = radio\n",
    "        self._temperatura = temperatura\n",
    "        self._distancia = distancia\n",
    "        self._movimiento_propio = movimiento_propio\n",
    "\n",
    "class Planeta:\n",
    "    def __init__(self, nombre, masa, radio):\n",
    "        self.nombre = nombre\n",
    "        self.masa = masa\n",
    "        self.radio = radio\n",
    "\n",
    "class SistemaPlanetario:\n",
    "    def __init__(self, *planetas):\n",
    "        self.estrellas = []\n",
    "        self.planetas = list(planetas)\n",
    "    \n",
    "    def agregar_estrella(self, estrella):\n",
    "        self.estrellas.append(estrella)\n",
    "    \n",
    "    def agregar_planeta(self, planeta):\n",
    "        self.planetas.append(planeta)\n",
    "    \n",
    "    def imprimir_informacion_publica(self):\n",
    "        print(\"Información pública de los sistemas planetarios:\")\n",
    "        for estrella in self.estrellas:\n",
    "            print(f\"Nombre: {estrella.nombre}, Masa: {estrella._masa}, Radio: {estrella._radio}, Temperatura: {estrella._temperatura}, Distancia: {estrella._distancia}, Movimiento propio: {estrella._movimiento_propio}\")\n",
    "        \n",
    "        print(\"Información pública de los planetas:\")\n",
    "        for planeta in self.planetas:\n",
    "            print(f\"Nombre: {planeta.nombre}, Masa: {planeta.masa}, Radio: {planeta.radio}\")\n",
    "\n",
    "def generar_nombre():\n",
    "    \"\"\"\n",
    "    Esta función genera un nombre aleatorio para una estrella o un planeta.\n",
    "    \"\"\"\n",
    "    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))\n",
    "\n",
    "def generar_estrella_aleatoria():\n",
    "    \"\"\"\n",
    "    Esta función genera una estrella con atributos aleatorios.\n",
    "    \"\"\"\n",
    "    nombre = generar_nombre()\n",
    "    masa = round(random.uniform(0.1, 100), 2)\n",
    "    radio = round(random.uniform(0.1, 50), 2)\n",
    "    temperatura = round(random.uniform(2000, 30000), 2)\n",
    "    distancia = round(random.uniform(10, 1000), 2)\n",
    "    movimiento_propio = round(random.uniform(0, 10), 2)\n",
    "    return Estrella(nombre, masa, radio, temperatura, distancia, movimiento_propio)\n",
    "\n",
    "def generar_planeta_aleatorio():\n",
    "    \"\"\"\n",
    "    Esta función genera un planeta con atributos aleatorios.\n",
    "    \"\"\"\n",
    "    nombre = generar_nombre()\n",
    "    masa = round(random.uniform(0.001, 10), 2)\n",
    "    radio = round(random.uniform(0.1, 5), 2)\n",
    "    return Planeta(nombre, masa, radio)\n",
    "\n",
    "def generar_sistema_planetario_aleatorio(num_estrellas, num_planetas):\n",
    "    \"\"\"\n",
    "    Esta función genera un sistema planetario con un número dado de estrellas y planetas aleatorios.\n",
    "    \"\"\"\n",
    "    sistema_planetario = SistemaPlanetario()\n",
    "    for _ in range(num_estrellas):\n",
    "        estrella = generar_estrella_aleatoria()\n",
    "        sistema_planetario.agregar_estrella(estrella)\n",
    "    for _ in range(num_planetas):\n",
    "        planeta = generar_planeta_aleatorio()\n",
    "        sistema_planetario.agregar_planeta(planeta)\n",
    "    return sistema_planetario\n",
    "\n",
    "# Ejemplo de uso\n",
    "sistema_aleatorio = generar_sistema_planetario_aleatorio(2, 3)\n",
    "sistema_aleatorio.imprimir_informacion_publica()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
