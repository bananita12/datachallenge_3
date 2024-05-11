{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
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
    "        return \", \".join(nombres_letras)"
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
