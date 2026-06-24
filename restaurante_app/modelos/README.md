# Sistema de Gestión de Restaurante

## Estudiante

Clide Alvarado

## Descripción

Este proyecto consiste en un sistema básico desarrollado en Python utilizando Programación Orientada a Objetos (POO). El sistema permite registrar productos y clientes de un restaurante mediante una estructura modular.

## Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py
```

## Clases implementadas

### Producto

Representa un producto disponible en el restaurante.

Tipos de datos utilizados:

- nombre → str
- precio → float
- categoria → str
- disponible → bool

### Cliente

Representa un cliente registrado.

Tipos de datos utilizados:

- nombre → str
- edad → int
- correo → str
- cliente_frecuente → bool

### Restaurante

Administra las listas de productos y clientes.

Utiliza listas para almacenar múltiples objetos.

## Conceptos aplicados

- Programación Orientada a Objetos
- Clases
- Objetos
- Constructores (__init__)
- Método especial __str__()
- Importaciones entre módulos
- Tipos de datos
- Listas
- Identificadores descriptivos
- Convenciones de nombres en Python

## Reflexión

Durante el desarrollo de esta actividad comprendí que utilizar identificadores descriptivos facilita la lectura y el mantenimiento del código. Además, el uso correcto de los tipos de datos y de las listas permite organizar mejor la información dentro de un proyecto modular. La Programación Orientada a Objetos ayuda a estructurar el software de manera ordenada y reutilizable.