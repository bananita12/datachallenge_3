{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cad85ad2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "class Estrella:\n",
    "    LSun = 3.828e26  # Solar luminosity in watts\n",
    "    MSun = 1.9884e30  # Solar mass in kilograms\n",
    "\n",
    "    def __init__(self, nombre, masa, radio, temperatura, distancia, movimiento_propio):\n",
    "        self.nombre = nombre\n",
    "        self._masa = masa\n",
    "        self._radio = radio\n",
    "        self._temperatura = temperatura\n",
    "        self._distancia = distancia\n",
    "        self._movimiento_propio = movimiento_propio\n",
    "\n",
    "    def calcular_luminosidad_total(self):\n",
    "        return 4 * np.pi * self._radio**2 * self._temperatura\n",
    "\n",
    "    def calcular_luminosidad_secuencia_principal(self):\n",
    "        return self.LSun * (self._masa / self.MSun)**3.5\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0328507a",
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
