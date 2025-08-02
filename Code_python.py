 *** Codigo para separar un DataFrame por medio de una funcion
from sklearn.model_selection import train_test_split

def train_val_test_split(df, size=0.3, rstate=42, shuffle=True, stratify=None):
    
    """
    Realiza un particionado de un DataFrame en tres subconjuntos: entrenamiento, validación y prueba.

    Parámetros:
    ------------
    * df : DataFrame
        El conjunto de datos que se desea dividir.

    * size : float, opcional (por defecto = 0.3)
        Proporción del conjunto de datos que se destinará a validación + prueba.
        El resto (1 - size) se usará para entrenamiento.
        Ejemplo: size = 0.3 → 70% train, 15% val, 15% test.

    * rstate : int, opcional (por defecto = 42)
        Semilla de aleatoriedad para reproducibilidad de resultados.

    * shuffle : bool, opcional (por defecto = True)
        Si True, mezcla aleatoriamente los datos antes de dividirlos.

    * stratify : string o None, opcional (por defecto = None)
        Nombre de la columna a usar para estratificación.
        Útil para asegurar que la proporción de clases se mantenga en cada subconjunto.
        Si es None, no se hace estratificación.

    Retorna:
    --------
    train_set : DataFrame
        Subconjunto para entrenamiento.

    val_set : DataFrame
        Subconjunto para validación.

    test_set : DataFrame
        Subconjunto para prueba.
    """
    strat = df[stratify] if stratify else None
    train_set, temp_set = train_test_split(
        df, test_size=size, random_state=rstate, shuffle=shuffle, stratify=strat)
    
    strat_2 = temp_set[stratify] if stratify else None
    val_set, test_set = train_test_split(
        temp_set, test_size=0.5, random_state=rstate, shuffle=shuffle, stratify=strat_2)
    
    return train_set, val_set, test_set


*** Codigo para hacer conteo del tiempo en que demora un Script
from time import perf_counter # Importa función de alta precisión para medir tiempo

# Marca el inicio del cronómetro (ejecución del notebook)
inicio = perf_counter()

# --- Aquí iría el contenido del notebook ---

# Marca el fin del cronómetro (cuando termina el notebook)
fin = perf_counter()
duracion = fin - inicio

# Convierte la duración en hora (3600seg), minutos y segundos
horas = int(duracion // 3600)
minutos = int((duracion % 3600) // 60)
segundos = duracion % 60

# Construye el mensaje según la duración
if horas > 0:
    print(f"⏱️ Notebook ejecutado en {horas}h {minutos}min {segundos:.2f}s")
elif minutos > 0:
    print(f"⏱️ Notebook ejecutado en {minutos}min {segundos:.2f}s")
else:
    print(f"⏱️ Notebook ejecutado en {segundos:.2f}s")





