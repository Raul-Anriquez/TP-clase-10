# Actividad Grupal - Patrones de Diseño

Comisión 3 - Programación Avanzada

Miembros del grupo:

- Marcos Manduca 47.555.520
- Hernan Sandroni 42.283.987
- Raul Anriquen 43.309.071
- Nicolas Alvarez Pacheco 46.744.923


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

Actividad 3 - Problemas cotidianos donde aplicar patrones de diseño

*Preparación de una comida en la cocina:

Problema
Al cocinar distintas recetas, algunos pasos son muy similares, pero otros cambian según el plato que se vaya a preparar.

Patrón aplicado: Template Method

El patrón Template Method permite definir una estructura general para realizar una tarea, pero dejando que algunos pasos cambien según la necesidad. Por ejemplo:
Para preparar una pizza → amasar, agregar ingredientes y hornear.
Para preparar una hamburguesa → cocinar carne, agregar ingredientes y servir.

*Pedido de comida por una aplicación
Problema

Un pedido pasa por distintas etapas: en preparación,enviado y recibido 

Patrón aplicado: State (Estado)

El patrón State permite que un objeto cambie su comportamiento según el estado en el que se encuentre. Por ejemplo, un pedido puede cambiar de acciones disponibles dependiendo de como se encuentre actualmente.

*Notificaciones en red social
Problema

Una red social quiere que al subir un estado o foto los seguidores de ese usuario reciban un aviso de forma automática 

Patrón aplicado: Observer (Observador)

El patrón Observer permite que un objeto notifique automáticamente a otros cuando ocurre un cambio en su estado

Actiividad 4 - Distintos nombres de patrones de diseño


# Patrones de Diseño

## Patrones Creacionales

| Patrón | También llamado | Descripción |
|---------|----------------|-------------|
| Factory Method | Método fábrica, Constructor virtual | Proporciona una interfaz para crear objetos en una superclase, permitiendo que las subclases modifiquen el tipo de objetos que se crearán. |
| Abstract Factory | Fábrica abstracta | Permite producir familias de objetos relacionados sin tener que especificar sus clases concretas. |
| Builder | Constructor | Permite construir objetos complejos paso a paso. Además, posibilita crear distintos tipos y representaciones de un objeto usando el mismo código de construcción. |
| Prototype | Prototipo, Clon, Clone | Permite copiar objetos existentes sin que el código dependa de sus clases concretas. |
| Singleton | Instancia única | Restringe la creación de objetos pertenecientes a una clase a un único objeto, asegurando que solo exista una única instancia del mismo. |

---

## Patrones Estructurales

| Patrón | También llamado | Descripción |
|---------|----------------|-------------|
| Adapter | Adaptador, Envoltorio, Wrapper | Permite que objetos con interfaces incompatibles puedan colaborar entre sí. |
| Bridge | Puente | Permite dividir una clase grande o un conjunto de clases estrechamente relacionadas en dos jerarquías separadas que pueden desarrollarse de forma independiente. |
| Composite | Objeto compuesto, Object Tree | Permite tratar objetos individuales y composiciones de objetos de manera uniforme, siendo especialmente útil para estructuras dinámicas en forma de árbol. |
| Decorator | Decorador, Envoltorio, Wrapper | Permite integrar más funciones o comportamientos en clases ya existentes. |
| Facade | Fachada | Proporciona una interfaz simplificada para interactuar con sistemas y subsistemas complejos. |
| Flyweight | Peso mosca, Peso ligero, Cache | Permite mantener más objetos dentro de la cantidad disponible de RAM compartiendo las partes comunes del estado entre varios objetos, en lugar de mantener toda la información en cada objeto. |
| Proxy | Sustituto, Marcador de posición | Permite proporcionar un sustituto o marcador de posición para otro objeto. Un proxy controla el acceso al objeto original, permitiendo realizar acciones antes o después de que la solicitud llegue al objeto original. |

---

## Patrones de Comportamiento

| Patrón | También llamado | Descripción |
|---------|----------------|-------------|
| Chain of Responsibility | Cadena de responsabilidad, CoR, Chain of Command | Permite pasar solicitudes a lo largo de una cadena de manejadores. Al recibir una solicitud, cada manejador decide si la procesa o si la pasa al siguiente manejador de la cadena. |
| Command | Comando, Orden, Action, Transaction | Convierte una solicitud en un objeto independiente que contiene toda la información sobre ella. Esta transformación permite parametrizar métodos con diferentes solicitudes, retrasar o poner en cola su ejecución y soportar operaciones que no se pueden realizar. |
| Iterator | Iterador | Permite recorrer los elementos de una colección sin exponer su representación subyacente. |
| Mediator | Mediador, Intermediary, Controller | Permite reducir las dependencias caóticas entre objetos. El patrón restringe las comunicaciones directas entre ellos, forzándolos a colaborar únicamente a través de un objeto que funciona como mediador. |
| Memento | Recuerdo, Instantánea, Snapshot | Permite guardar y restaurar el estado previo de un objeto sin revelar los detalles de su implementación. |
| Observer | Observador, Publicación-Suscripción, Modelo-patrón, Event-Subscriber, Listener | Permite definir un mecanismo de suscripción para notificar a varios objetos sobre cualquier evento que ocurra en el objeto que está siendo observado. |
| State | Estado | Permite a un objeto cambiar su comportamiento cuando su estado interno cambia. |
| Strategy | Estrategia | Permite definir un grupo de algoritmos, colocarlos en clases separadas y hacer sus objetos intercambiables. |
| Template Method | Método plantilla | Define el esqueleto de un algoritmo en una superclase, pero permite que las subclases sobrescriban pasos del algoritmo sin cambiar su estructura. |
| Visitor | Visitante | Permite separar algoritmos de los objetos sobre los que operan. |

# Actividad 5

Un **antipatrón** es una solución que parece lógica o rápida en el momento, pero que a largo plazo genera problemas de mantenimiento, rendimiento o escalabilidad. Básicamente, son **malas prácticas** que se han vuelto comunes en el desarrollo de software.

### Código Espagueti (Spaghetti Code)
Es cuando la lógica del programa está tan enredada y carece de estructura que resulta difícil seguir el flujo de ejecución, comprender el funcionamiento del sistema o realizar modificaciones sin introducir errores.

### Objeto Dios (God Object)
Ocurre cuando una sola clase, módulo o archivo intenta realizar prácticamente todas las tareas del sistema. Al concentrar demasiadas responsabilidades, cualquier cambio puede afectar múltiples funcionalidades y aumentar el riesgo de fallos.

### Hard Coding
Es la práctica de dejar valores críticos escritos directamente en el código fuente, como contraseñas, rutas de acceso o direcciones URL. Esto vuelve al sistema rígido y difícil de mantener, ya que cualquier cambio requiere modificar y recompilar el programa.

### Flujo de Lava (Lava Flow)
Se refiere a la acumulación de código antiguo, funciones o módulos que ya no se entienden completamente, pero que permanecen en el sistema porque existe el temor de que eliminarlos provoque errores o fallos inesperados.
