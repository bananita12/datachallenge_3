{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "88f6749e",
   "metadata": {},
   "outputs": [],
   "source": [
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
    "        pass"
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
