{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cae49843",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Planeta' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [2]\u001b[0m, in \u001b[0;36m<cell line: 2>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m#para este codigo se necesita una clase planeta y una clase estrella\u001b[39;00m\n\u001b[0;32m----> 2\u001b[0m \u001b[38;5;28;01mclass\u001b[39;00m \u001b[38;5;21;01mExoplaneta\u001b[39;00m(\u001b[43mPlaneta\u001b[49m):\n\u001b[1;32m      3\u001b[0m     \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mmetodo_primer_descubrimiento\u001b[39m(\u001b[38;5;28mself\u001b[39m, metodo):\n\u001b[1;32m      4\u001b[0m         \u001b[38;5;66;03m# Método de primer descubrimiento: \"imagen directa\", \"velocidad radial\" o \"tránsito\"\u001b[39;00m\n\u001b[1;32m      5\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m metodo\n",
      "\u001b[0;31mNameError\u001b[0m: name 'Planeta' is not defined"
     ]
    }
   ],
   "source": [
    "#para este codigo se necesita una clase planeta y una clase estrella\n",
    "class Exoplaneta(Planeta):\n",
    "    def metodo_primer_descubrimiento(self, metodo):\n",
    "        # Método de primer descubrimiento: \"imagen directa\", \"velocidad radial\" o \"tránsito\"\n",
    "        return metodo\n",
    "\n",
    "    def es_similar_tatooine(self):\n",
    "        if isinstance(self._anfitriona, Estrella) and self._anfitriona.nombre.lower() == \"binaria\":\n",
    "            return True\n",
    "        return False\n",
    "    def parametro_impacto_b(self):\n",
    "        if self.metodo_descubrimiento() == \"tránsito\":\n",
    "            a = 1  # Distancia orbital del planeta alrededor de la estrella (en UA)\n",
    "            e = 0  # Excentricidad de la órbita\n",
    "            i = np.radians(90)  # Inclinación orbital (en radianes)\n",
    "            omega = 0  # Argumento del periastron\n",
    "            R_star = 1  # Radio estelar (en UA)\n",
    "            b = a * np.cos(i) / ((1 - e**2) * (R_star * (1 + e * np.sin(omega))))\n",
    "            return b\n",
    "def ejemplo_clase_exoplaneta():\n",
    "    # Crear una instancia de la clase Exoplaneta\n",
    "    planeta_ejemplo = Exoplaneta(nombre=\"Ejemplo\", masa=1.898e27, radio=7.149e7, anfitriona=Estrella(nombre=\"Anfitriona\", masa=2.2e30, radio=6.9634e8, temperatura=5778, distancia=0, movimiento_propio=0))\n",
    "\n",
    "    # Llamar al método para obtener el método de primer descubrimiento y mostrarlo\n",
    "    metodo_descubrimiento = planeta_ejemplo.metodo_primer_descubrimiento(\"velocidad radial\")\n",
    "    print(\"Método de primer descubrimiento del planeta de ejemplo:\", metodo_descubrimiento)\n",
    "\n",
    "    # Verificar si el planeta de ejemplo es similar a Tatooine\n",
    "    similar_tatooine = planeta_ejemplo.es_similar_tatooine()\n",
    "    if similar_tatooine:\n",
    "        print(\"El planeta de ejemplo es similar a Tatooine.\")\n",
    "    else:\n",
    "        print(\"El planeta de ejemplo no es similar a Tatooine.\")\n",
    "\n",
    "# Llamar a la función de ejemplo\n",
    "ejemplo_clase_exoplaneta()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "195e7c2a",
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
