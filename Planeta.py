{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "88f6749e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Estrella' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [1]\u001b[0m, in \u001b[0;36m<cell line: 45>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     42\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLuminosidad en la secuencia principal de la estrella anfitriona:\u001b[39m\u001b[38;5;124m\"\u001b[39m, planeta\u001b[38;5;241m.\u001b[39mluminosidad_sec_principal())\n\u001b[1;32m     44\u001b[0m \u001b[38;5;66;03m# Ejecutamos el ejemplo\u001b[39;00m\n\u001b[0;32m---> 45\u001b[0m \u001b[43mejemplo_uso_planeta\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "Input \u001b[0;32mIn [1]\u001b[0m, in \u001b[0;36mejemplo_uso_planeta\u001b[0;34m()\u001b[0m\n\u001b[1;32m     26\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mejemplo_uso_planeta\u001b[39m():\n\u001b[1;32m     27\u001b[0m     \u001b[38;5;66;03m# Creamos una estrella como anfitriona del planeta\u001b[39;00m\n\u001b[0;32m---> 28\u001b[0m     estrella \u001b[38;5;241m=\u001b[39m \u001b[43mEstrella\u001b[49m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSol\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;241m1.989e30\u001b[39m, \u001b[38;5;241m6.957e8\u001b[39m)\n\u001b[1;32m     30\u001b[0m     \u001b[38;5;66;03m# Creamos un planeta orbitando la estrella\u001b[39;00m\n\u001b[1;32m     31\u001b[0m     planeta \u001b[38;5;241m=\u001b[39m Planeta(estrella, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTierra\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;241m5.972e24\u001b[39m, \u001b[38;5;241m6.371e6\u001b[39m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'Estrella' is not defined"
     ]
    }
   ],
   "source": [
    "#introducir una clase estrella\n",
    "class Planeta:\n",
    "    def __init__(self, anfitriona, nombre, masa, radio):\n",
    "        self.nombre = nombre\n",
    "        self.masa = masa\n",
    "        self.radio = radio\n",
    "        self._anfitriona = anfitriona\n",
    "\n",
    "    def luminosidad(self):\n",
    "        return self._anfitriona.calcular_luminosidad_total()\n",
    "\n",
    "    def luminosidad_sec_principal(self):\n",
    "        return self._anfitriona.calcular_luminosidad_secuencia_principal()\n",
    "\n",
    "    def period_rot_kepler(self):\n",
    "        # Define this method based on your needs\n",
    "        pass\n",
    "\n",
    "    def metodo_descubrimiento(self):\n",
    "        # Define this method based on your needs\n",
    "        pass\n",
    "\n",
    "    def tatooine(self):\n",
    "        # Define this method based on your needs\n",
    "        pass\n",
    "\n",
    "def ejemplo_uso_planeta():\n",
    "    # Creamos una estrella como anfitriona del planeta\n",
    "    estrella = Estrella(\"Sol\", 1.989e30, 6.957e8)\n",
    "\n",
    "    # Creamos un planeta orbitando la estrella\n",
    "    planeta = Planeta(estrella, \"Tierra\", 5.972e24, 6.371e6)\n",
    "\n",
    "    # Mostramos información sobre el planeta\n",
    "    print(\"Nombre del planeta:\", planeta.nombre)\n",
    "    print(\"Masa del planeta:\", planeta.masa)\n",
    "    print(\"Radio del planeta:\", planeta.radio)\n",
    "\n",
    "    # Calculamos y mostramos la luminosidad total de la estrella anfitriona\n",
    "    print(\"Luminosidad total de la estrella anfitriona:\", planeta.luminosidad())\n",
    "\n",
    "    # Calculamos y mostramos la luminosidad en la secuencia principal de la estrella anfitriona\n",
    "    print(\"Luminosidad en la secuencia principal de la estrella anfitriona:\", planeta.luminosidad_sec_principal())\n",
    "\n",
    "# Ejecutamos el ejemplo\n",
    "ejemplo_uso_planeta()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "607a7bfb",
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
