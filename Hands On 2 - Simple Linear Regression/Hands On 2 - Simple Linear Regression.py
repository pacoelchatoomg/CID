#Gerson Alberto Correa Peña
#CID
#Hands On 2 : Simple Linear Regression


class RegresionLinealSimple:
    def __init__(self, advertising, sales):     #Inicializar valores
        self.advertising = advertising            
        self.sales = sales
        self.beta_0 = 0                         #Termino independiente o intercepto
        self.beta_1 = 0                         #Pendiente o coeficiente
        self._entrenar()

    def _entrenar(self):
        #Calcular la media de advertising(x) y sales(y)                        
        n = len(self.advertising)
        media_x = sum(self.advertising) / n
        media_y = sum(self.sales) / n

        #Formula de minimos cuadrados (numerador es la covarianza entre X y Y y denominador es varianza de X)
        numerador = sum((self.advertising[i] - media_x) * (self.sales[i] - media_y) for i in range(n))             
        denominador = sum((self.advertising[i] - media_x) ** 2 for i in range(n))

        #Calcula la pendiente b1 y el intercepto b0.
        self.beta_1 = numerador / denominador
        self.beta_0 = media_y - self.beta_1 * media_x

        #Predecir Y(sales) dado X(advertising) 
    def predecir(self, x):
        return self.beta_0 + self.beta_1 * x
        #Muestra la ecuación final del modelo, con los valores calculados de b0 y b1.
    def imprimir_ecuacion(self):
        print(f" Ecuacion: ŷ = {self.beta_0:.4f} + {self.beta_1:.4f}x")


# Datos del Caso Benetton
datos_advertising = [23, 26, 30, 34, 43, 48, 52, 57, 58]
datos_sales = [651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518]

# Crear modelo
modelo = RegresionLinealSimple(datos_advertising, datos_sales)

# Imprimir la ecuación de regresión
modelo.imprimir_ecuacion()

# Predicciones para nuevos valores de advertising
nuevos_valores_advertising = [25, 35, 40, 50, 60]
print("\nPredicciones:")
for x in nuevos_valores_advertising:
    prediccion = modelo.predecir(x)
    print(f"advertising = {x} → Predicción de sales = {prediccion:.2f} millones de euros")