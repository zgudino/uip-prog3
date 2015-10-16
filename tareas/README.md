# ¿Qué es \__main__ y cómo funciona?

#### Concepto
> Las buenas practicas sugieren al menos encapsular un bloque de código dentro de `__main__` ejemplo como *bootstrapping* de la aplicación.

`__main__` es una variable de alto-nivel la cual representa el scope del programa principal a ejecutar por el interpretador.

El concepto es similar a `main()` en otros lenguajes de programación sin embargo, muy distinto en comportamiento; Python `__main__` es opcional, interpretador piadosamente ejecutara el fuente.

Las buenas practicas sugieren al menos encapsular un bloque de código dentro de `__main__` ejemplo como *bootstrapping* de la aplicación. 

#### Funcionamiento
> Luego, el interpretador inicializa la variable de ambiente `__name__` asignando el valor `__main__`.

Cuando el interpretador ejecuta un programa primero ejecuta un archivo fuente _.py_.

Luego, el interpretador inicializa la variable de ambiente `__name__` asignando el valor `__main__`. De ahora en adelante, la variable es referenciada a este fuente.

###### Ejemplo

```python
# b.py
def say(msg: str) -> str:
    try:
        if not (msg is not None or not msg == ""):
            raise Exception("Error: Argumento << msg >> es vacio")

        print(msg)
    except ValueError as err:
        print(err, err.__cause__)


if __name__ == "__main__":
    from playground.mods.a import happy

    happy()
```

```python
# a.py
import playground.mods.b as b


def happy(msg="I'm very happy now!"):
    b.say(msg)


if __name__ == "__main__":
    b.say("Hola \nMensaje desde modulo %s" % __name__)
```

Si ejecutamos el fuente **b.py**

```sh
❯ python3 b.py
I'm very happy now!
```

Por otro lado, ejecutamos el fuente **a.py**

```sh
❯ python3 a.py
Hola
Mensaje desde modulo __main__
```

Claramente observamos el beneficio de `__main__` cuando el programa utiliza módulos.