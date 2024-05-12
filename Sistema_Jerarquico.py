{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9d1a31ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "class SistemaJerarquico:\n",
    "    def __init__(self, *estrellas):\n",
    "        self.estrellas = list(estrellas)\n",
    "\n",
    "    def estrellas_ordenadas_por_masa(self):\n",
    "        return sorted(self.estrellas, key=lambda x: x._masa)\n",
    "\n",
    "    def nombres_estrellas_letras_ordenadas(self):\n",
    "        letras = \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n",
    "        nombres = [estrella.nombre for estrella in self.estrellas]\n",
    "        nombres_letras = [f\"{nombre}{letra}\" for nombre, letra in zip(nombres, letras)]\n",
    "        return \", \".join(nombres_letras)\n",
    "def explicar_clase_sistema_jerarquico():\n",
    "    \"\"\"\n",
    "    Esta función explica la funcionalidad de la clase SistemaJerarquico.\n",
    "\n",
    "    La clase SistemaJerarquico representa un sistema que contiene múltiples estrellas.\n",
    "    Permite realizar dos operaciones principales:\n",
    "\n",
    "    1. estrellas_ordenadas_por_masa():\n",
    "        - Esta función ordena las estrellas dentro del sistema por su masa de manera ascendente.\n",
    "        - Devuelve una lista de estrellas ordenadas por masa.\n",
    "\n",
    "    2. nombres_estrellas_letras_ordenadas():\n",
    "        - Esta función genera nombres para las estrellas basados en una secuencia de letras del alfabeto.\n",
    "        - Asigna a cada estrella un nombre que combina su nombre original con una letra del alfabeto, en orden.\n",
    "        - Devuelve una cadena que contiene los nombres de las estrellas junto con las letras correspondientes.\n",
    "\n",
    "    En resumen, la clase SistemaJerarquico proporciona métodos para ordenar las estrellas por masa\n",
    "    y asignar nombres a las estrellas utilizando letras del alfabeto.\n",
    "    \"\"\"\n",
    "    print(explicar_clase_sistema_jerarquico.__doc__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2046e65",
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
