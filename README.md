# Sistema de Servicio Técnico de Equipos Informáticos  
Aplicación web desarrollada con **Python / Django** y base de datos **SQLite3**

## 📌 Descripción

Este proyecto es una aplicación web para gestionar un **servicio técnico de equipos informáticos**.  
Permite registrar clientes, equipos, órdenes de servicio y el seguimiento completo del mantenimiento realizado.

Ha sido desarrollado con el framework **Django** (Python) utilizando **SQLite3** como base de datos por defecto, lo que facilita la instalación y las pruebas en entornos locales sin necesidad de configurar un servidor de base de datos externo.

Está orientado a talleres de reparación, centros de cómputo, laboratorios técnicos o pequeños negocios que necesitan controlar sus órdenes de mantenimiento de forma sencilla y centralizada.

---

## 🚀 Funcionalidades principales

- Gestión de **clientes** (alta, edición, listado, búsqueda).
- Registro de **equipos** asociados a cada cliente.
- Creación y administración de **órdenes de servicio / mantenimiento**.
- Estados de la orden: por ejemplo, *pendiente*, *en revisión*, *en reparación*, *finalizado*, *entregado*.
- Registro de diagnóstico, actividades realizadas y observaciones.
- Control de fechas de ingreso y salida del equipo.
- Listados y filtros por cliente, estado o rango de fechas.
- Panel básico de administración usando el **Django Admin**.
- Autenticación de usuarios (login/logout) para proteger el acceso al sistema.

---
## 🛠 Tecnologías utilizadas

- **Python 3.x**
- **Django 3.x / 4.x** (según la versión que uses)
- **SQLite3** (base de datos por defecto de Django)
- **HTML / CSS / Bootstrap** (para la interfaz)
- **Django Admin** para gestión interna

---

## 📁 Estructura básica del proyecto

```text
/proyecto_servicio_tecnico
    /servicio_tecnico           # App principal del sistema
    /proyecto                   # Configuración del proyecto Django
    /templates                  # Plantillas HTML
    /static                     # Archivos estáticos (CSS, JS, imágenes)
    db.sqlite3                  # Base de datos SQLite
    manage.py
    README.md
