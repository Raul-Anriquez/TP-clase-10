# Actividad Grupal - Patrones de Diseño

Comisión 3 - Programación Avanzada

Miembros del grupo:

- Marcos Manduca 47.555.520
- Hernan Sandroni
- Raul Anriquen 43.309.071
- Nicolas Alvarez Pacheco


**1) Investigar y documentar críticas a los patrones de diseño. Mencione ejemplos concretos.**

A pesar de que los patrones de diseño son reutilizables para problemas frecuentes en software, algunos desarrolladores consideran que puede generar complejidad innecesaria si se abusa de estos.

## Complejidad innecesaria

Aplicar patrones para problemas simples. Esto hace que el programa sea mas dificil de leer y entender visualmente.

### Ejemplo

En vez de:

```python
usuario = Usuario()
```

crear:

```python
usuario = UsuarioFactory.crear_usuario()
```

Aunque nunca existá otro tipo de usuario. Esto genera clase y metodos que no aportan al software.

## Sobreingeniería (Overengineering)

Aplicar patrones de forma preventida (por asi acaso) cuando quizas nunca pasen.

### Ejemplo

Crear una jerarquia enorme de clases porque "algun día podría crecer"

Clase Vehiculo
- Auto
- Camion
- Moto
- Camioneta
- AutoDeportivo
- AutoElectrico
- ...

Cuando el programa solo necesita manejar autos. Aumenta tiempo de desarrollo y mantenimiento.

## Aumento del número de clases 

Muchos patrones pueden generar más clases, interfaces y archivos.

### Ejemplo

Un Factory simple puede necesitar:

- Producto
- ProductoA
- ProductoB
- Factory
- Main

Para una tarea sencilla. Hace el proyecto mas complicado de manejar. 

## Pueden ocultar soluciones más simples.

A veces una funcion o una clase simple puede resolver el problema mejor que un patrón completo.

### Ejemplo

Usar un Singleton para una configuración: 

```config = Configuracion()```

Podría ser suficiente sin implementar toda la lógica del patrón. Lo cual vuelve el codigo mas complejo de lo necesario. 

## NO son reglas obligatorias.

Muchos principiantes intentan aplicar patrones a todo, como un Factory, Singleton y Observer a un programa sencillo de consola.
Los patrones son herramientas, no requisitos

Los patrones de diseño son útiles para resolver problemas comunes en desarrollo de software. Pero, utilizarlos sin una necesidad real termina generando complejidad innecesaria, aumento de la cantidad de clases y dificultad para el mantenimiento del código. Por este motivo, se recomienda aplicarlos únicamente cuando aporten una mejora clara en la organización. 

**2) Seleccione 3 patrones de diseño e implementarlos en Python. Arme ejemplos concretos de uso. Lo ideal es elegir un patrón de cada clasificación.**

## Patrón Singleton (Creacional)

### Descripción

El patrón Singleton garantiza que una clase tenga una única instancia durante toda la ejecución del programa y proporciona un punto de acceso global a dicha instancia.

### Problema que resuelve

En algunos sistemas es necesario evitar la creación de múltiples objetos de una misma clase. Un ejemplo común es una configuración global de la aplicación.

### Implementación

Se implementó una clase `Configuracion` utilizando el método especial `__new__()`, el cual controla la creación de nuevas instancias. Si ya existe una instancia, se devuelve la misma en lugar de crear otra.

### Ejemplo de uso

Se crearon dos variables (`config1` y `config2`) y se comprobó que ambas referencian el mismo objeto. Al modificar una configuración desde una variable, el cambio se refleja en la otra.

Implementación en `singleton.py`

---

## Patrón Adapter (Estructural)

### Descripción

El patrón Adapter permite que clases con interfaces incompatibles puedan trabajar juntas mediante una clase adaptadora.

### Problema que resuelve

Muchas veces se utilizan bibliotecas o componentes externos cuyos métodos no coinciden con los que espera nuestra aplicación. El Adapter traduce una interfaz en otra sin modificar el código original.

### Implementación

Se utilizó una clase `Spotify` con un método `play()`. Luego se creó una clase `SpotifyAdapter` que traduce las llamadas hacia el método esperado por el programa (`reproducir()`).

### Ejemplo de uso

La aplicación interactúa únicamente con el método `reproducir()`, mientras que el adaptador se encarga de invocar internamente `play()`.

Implementación en `adapter.py`

---

## Patrón Observer (Comportamiento)

### Descripción

El patrón Observer establece una relación de uno a muchos entre objetos. Cuando un objeto cambia de estado, todos los objetos suscritos son notificados automáticamente.

### Problema que resuelve

Permite mantener sincronizados varios objetos sin que exista una dependencia fuerte entre ellos.

### Implementación

Se desarrolló una clase `Canal` que mantiene una lista de suscriptores. Cada suscriptor posee un método `actualizar()` que recibe las notificaciones.

### Ejemplo de uso

Cuando el canal publica un nuevo video mediante `subir_video()`, todos los suscriptores reciben automáticamente una notificación indicando el contenido publicado.

Implementación en `observer.py`


