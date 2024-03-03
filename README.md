# GESTIÓN DE EVENTOS

## URL del repositorio

[https://github.com/Argueth/gestion_eventos](https://github.com/Argueth/gestion_eventos)

## Proceso de instalación:

El módulo Gestión de Eventos depende del módulo **hr** para acceder a los empleados y poder agregarlos a un evento. Para poder hacer esto es necesario instalar, previamente, el módulo **hr**.
Además, para acceder a los Clientes y los Proveedores, es necesario instalar el módulo **Contacts** (En caso de tener el módulo Facturación esta dependencia ya estará satisfecha).

### Esquema de dependencias:
- base
- contacts
    - res.partner
- hr
    - hr.employee

### Orden del Proceso:
- Accede al servidor web en el que tengas instalado OdooDock. Si lo tienes en un contenedor, el código será algo como esto:
```shell
docker exec -it [nombre de tu servicio web] bash
```
- Accede a la carpeta extra-addons:
```bash
cd mnt/extra-addons
```
- Clona el repositorio que contiene el módulo Gestión de Eventos:
```bash
git clone https://github.com/Argueth/gestion_eventos.git
```
A partir de este momento ya aparecerá el módulo en la **lista de aplicaciones** de tu sistema Odoo. Sin embargo, antes de instalarlo deberás tener en cuenta las **dependencias** que tiene este módulo (ver apartado **Esquema de dependencias**). 
Para ello sigue las siguientes instrucciones: 
- Instalar el módulo **hr** (Empleados)
    - Crear, por lo menos, los departamentos sigientes:
        - Iluminación
        - Sonido
        - Montaje
        - Dirección
        - Gestión de Eventos
    - Añadir empleados a estos departamentos
    - Crear usuarios de Odoo para los empleados que la empresa vea conveniente que tenga usuario.
- Instalar el módulo **contacts** (Facturación)
- Instalar el módulo **gestion_eventos** (Gestión de Eventos)
    - Dar permisos a los empleados dependiendo de lo que se quiera permitir a cada usuario (ver apartado **Información de permisos**).

### Información de permisos:
Gestión de Eventos creara en el sistema una categoría de permisos llamada **Gestion Eventos** a la que se podrá acceder desde la configuración de usuarios de Odoo.
Creará también cuatro grupos, correspondientes a las opciones contenidas dentro de la categoría ya mencionada y cada uno tendrá unos permisos específicos. 
#### Listado de roles y permisos:
- **Comercial**:
    - Permisos totales en los eventos.
    - Permisos totales para los materiales.
    - Permisos totales para los tipos de evento.
    - Permisos totales para las plantillas de presupuesto.
    - Permisos totales para los presupuestos de evento.
    - Permisos totales para las lineas de presupuesto.
    - Permiso para ver las fases de un evento pero no modificarlas, crearlas o eliminarlas.
    - Permiso para ver los empleados de iluminación, sonido y montaje asignados a los eventos.
- **Technic**:
    - Permiso para ver los eventos.
    - Permiso para ver los materiales.
    - Permiso para ver los tipos de evento.
    - Ningún permiso para las plantillas de presupuesto.
    - Ningún permiso para los presupuestos de evento.
    - Ningún permiso para las líneas de presupuesto.
    - Permiso para ver las fases de un evento pero no modificarlas, crearlas o eliminarlas.
    - Permiso para ver los empleados de iluminación, sonido y montaje asignados a los eventos.
- **Event Manager**:
    - Permisos para ver y modificar los eventos, pero no crearlos ni eliminarlos.
    - Permisos para ver y modificar los materiales.
    - Permisos para ver y modificar los tipos de evento.
    - Permiso para ver las plantillas de presupuesto.
    - Permisos totales para los presupuestos de evento.
    - Permisos totales para las lineas de presupuesto.
    - Permisos totales para las fases de un evento.
    - Permisos totales para los empleados de iluminación, sonido y montaje asignados a los eventos.
- **Director**:
    - Permisos para ver y modificar y eliminar los eventos pero no crearlos.
    - Permisos para ver los materiales.
    - Permisos para ver los tipos de evento.
    - Permiso para ver y modificar las plantillas de presupuesto.
    - Permiso para ver los presupuestos de evento.
    - Permiso para ver las lineas de presupuesto.
    - Permiso para ver las fases de un evento pero no modificarlas, crearlas o eliminarlas.
    - Permisos para ver los empleados de iluminación, sonido y montaje asignados a los eventos. 