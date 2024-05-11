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
   "source": []
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
