{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cad85ad2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Luminosidad total del Sol: 3.5142399235508362e+22\n",
      "Luminosidad en la secuencia principal del Sol: 3.828e+26\n"
     ]
    }
   ],
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
    "        return self.LSun * (self._masa / self.MSun)**3.5\n",
    "\n",
    "def ejemplo_clase_estrella():\n",
    "    sol = Estrella(nombre=\"Sol\", masa=1.9884e30, radio=6.957e8, temperatura=5778, distancia=0, movimiento_propio=0)\n",
    "    # Calcular la luminosidad total y mostrarla\n",
    "    luminosidad_total = sol.calcular_luminosidad_total()\n",
    "    print(\"Luminosidad total del Sol:\", luminosidad_total)\n",
    "    # Calcular la luminosidad en la secuencia principal y mostrarla\n",
    "    luminosidad_secuencia_principal = sol.calcular_luminosidad_secuencia_principal()\n",
    "    print(\"Luminosidad en la secuencia principal del Sol:\", luminosidad_secuencia_principal)\n",
    "    # Llamar a la función de ejemplo\n",
    "ejemplo_clase_estrella()\n",
    "\n",
    "    "
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
