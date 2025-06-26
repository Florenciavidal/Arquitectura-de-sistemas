# Sistema de Detección de Fallas HTTP

Este sistema simula una arquitectura cliente-balanceador-servidores con Flask para detectar errores HTTP comunes:

## Componentes

- `app.py`: servidores Flask (puertos 5001 y 5002)
- `load_balancer.py`: balanceador de carga (puerto 8080)
- `test_errors.py`: script de pruebas
- `errors/stats`: endpoint para estadísticas

## Tipos de errores detectados

| Código | Tipo            | Causa                        |
|--------|------------------|------------------------------|
| 400    | BAD REQUEST      | JSON vacío                   |
| 404    | NOT FOUND        | Ruta no existe               |
| 500    | INTERNAL ERROR   | Error interno del servidor   |

## Uso

# Terminal 1
python app.py 5001

# Terminal 2
python app.py 5002

# Terminal 3
python load_balancer.py

# Terminal 4
python test_errors.py
