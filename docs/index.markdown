---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

# GESTIÓN DE EVENTOS

# Nombre técnico:
> gestion_eventos

# Descripción corta:
> Este módulo permite al gestor de eventos seleccionar el equipo que se usará en un evento, las personas que participarán en él y en qué horarios de entre los eventos que agregue el departamento comercial.

# Descripción detallada de todas sus funciones:
>
- ## **Comercial:**
    - Agregar un evento nuevo:
        - Poner nombre al nuevo evento.
        - Poner fechas al nuevo evento: Se podrá indicar la fecha de estreno del evento y, si se ha pactado con el cliente, el periodo de montraje y preparación y el tiempo de desmontaje (si es más de un día).
        - Indicar aspectos hablados y pactados con el cliente: Se debe poder indicar consideraciones especiales que se hayan hablado con el cliente.
        
>
- ## **Gestor de eventos:**
    - Ver los eventos en activo.
    - Editar eventos:
        - Ver equipo disponible: El gestor de eventos debe poder ver qué equipo estará disponible en el momento del evento (día del evento) para poder seleccionarlo.
        - Agregar equipo que se usará: Se podrá seleccionar, de entre el equipo disponible, cuál será el usado en el evento y, al ser seleccionado, aparecerá como no disponible en las fechas indicadas para el evento.
        - Agregar personal técnico que participará en el evento: El personal debe aparecer como no ocupado en otro evento. Se deberá poder ver todo el personal, pero con el indicativo de si está o no ocupado y, en caso afirmativo, en qué evento está ocupado a esa hora en esa fecha concreta.
        - Fijar horarios orientativos: Se deberá poder indicar el tiempo de cada fase del evento (días de montaje, día y hora de estreno, duración de la función, etc...)
        - Establecer una ubicación para el evento: el módulo deberá permitir indicar una ubicación del evento para que los trabajadores sepan donde han de dirigirse.
        - Marcar indicaciones para los técnicos de luces: Se deberá poder agregar indicaciones para los técnicos de iluminación, así como adjuntar el plano de montaje de iluminación del evento.
        - Marcar indicaciones para los técnicos de sonido: Se deberá poder agregar indicaciones para los técnicos de sonido, así como adjuntar el plano de montaje de sonido del evento.
        - Marcar indicaciones para los técnicos de montaje (incluidos riggers): Se deberá poder agregar indicaciones para los técnicos de montaje, así como adjuntar el plano de montaje de estructuras del evento.
    - Cambiar al personal de un evento a otro: Se deberá poder cambiar al personal de un evento a otro (siempre con una semana de antelación) para poder hacer frente a situaciones de mucho volumen de trabajo.
    - Se deberá poder tener acceso al contacto de personal temporal de la empresa: Se debe poder tener acceso al contacto de los técnicos que trabajan esporádicamente para la empresa para contactar con ellos en caso de que sean necesarios y poder incluirles en el evento.
- ## **Responsable de iluminaión del evento:**
    - El módulo deberá mostrar a este la lista de material de iluminación que ha sido asignado al evento o También debe mostrar la lista de personal de iluminación
    - Debemostrarloshorarios,
    - Debe mostrar los archivos adjuntos referentes a la iluminación
    - Debe mostrar la ubicación del evento
- ## **Responsable de sonido del evento:**
    - El módulo deberá mostrar a este la lista de material de sonido que ha sido asignado al evento o También debe mostrar la lista de personal de sonido
    - Debemostrarloshorarios
    - Debe mostrar los archivos adjuntos referentes al sonido
    - Debe mostrar la ubicación del evento
- **Responsable de montaje del evento:**
    - El módulo deberá mostrar a este la lista de material de montaje que ha sido asignado al evento o También debe mostrar la lista de personal de iluminación
    - Debemostrarloshorarios
    - Debe mostrar los archivos adjuntos referentes a la iluminación
    - Debe mostrar la ubicación del evento
- ## **Responsable de transporte de material/transportista/conductor:**
    - El módulo debe mostrar la lista completa del material (iluminación, sonido y montaje) que ha de ser llevado a la ubicación del evento
    - Debe mostrar también la ubicación del evento
    - Debe mostrar los horarios y fechas (carga en el almacén, transporte y descarga en la ubicación del evento; recogida en el lugar del evento, transporte y descarga en el almacén)
- ## **Almacén:**
    - Debe poder ver la lista de eventos, las fechas y el material necesario. 
    - Marcar el material como preparado 
    - Marcar posibles incidencias
- ## **Técnicos:**
    - Estaría bien si mostrase algún tipo de lista u horario a cada técnico para que sepa exactamente dónde debe estar en cada momento en caso de que tenga que ir a más de un evento en un solo día. (No sé si eso es mejor que lo lleve el responsable de cada departamento y no marear a los técnicos con el software).

# Mapa del módulo: 
> ![](img/modulo_grande_mapa.drawio.png)

# Dependencias de otros módulos:
> Este módulo depende de la tabla de empleados del módulo “Empleados”. Deberá recoger la mencionada tabla para poder acoplar los empleados disponibles a eventos y de la tabla clientes del módulo “Clientes”. Deberá recoger la mencionada tabla para poder vincular los clientes a los eventos.

# Wireframes:
> 
## **Pantalla general de eventos:** 
Esta sería la pantalla inicial del módulo. Todos los usuarios que entrasen verían la misma
pantalla, pero con un contenido diferente.
- Comercial: Vería la lista completa de eventos con las fechas de los mismos y tendría habilitado el botón “Crear”.
- Gestor de eventos: Vería la lista completa de eventos y tendría habilitado el botón de “Editar”.
- Responsables de los diferentes departamentos: Verían la lista de los eventos en los que apareciesen como
personal y, al pulsar en alguno de ellos, verían la información del evento referente a su departamento y la temporalización.
>
![](img/PANTALLA%20DE%20GENERACIÓN%20DE%20EVENTOS.drawio.png)
## **Pantalla de creación de un nuevo evento:**
 Esta pantalla es la que vería el comercial al pulsar sobre el botón “Crear” en la pantalla anterior. El comercial tendría que rellenar los cuadros de información con el nombre del evento (deberá ser único y no existir en la base de datos para ser válido), los datos del cliente (que son nombre, teléfono, email, dirección), la ubicación del evento y una lista de posibles fechas pactadas con el cliente (fecha de inicio de montaje, periodo máximo de montaje, estreno, fecha límite para dejar libre el espacio). Para añadir una nueva línea a la lista de fechas podrá utilizar el botón “Añadir fecha” y se le habilitará una nueva línea en la lista, donde podrá introducir los datos de la nueva fecha (motivo, fecha y hora de inicio, fecha y hora de fin, observaciones). Cuando haya terminado podrá utilizar el botón “Guardar” para guardar el nuevo evento y que aparezca en la lista de la pantalla general de eventos o el botón “Descartar”, con el que eliminaría el nuevo evento y volvería a la pantalla general de eventos.
>
![](img/PANTALLA%20DE%20CREACIÓN%20DE%20UN%20NUEVO%20EVENTO.drawio.png)
## **Pantalla de edición de eventos:**
Esta pantalla es la que vería el Gestor de Eventos si selecciona un evento en la pantalla general de eventos y pulsa el botón “Editar”. En esta pantalla podrá ver los datos del cliente y una seria de pestañas correspondientes a los diferentes departamentos y la temporalización. Dentro de cada departamento podrá añadir personal y material que deberá estar libre en las fechas del evento (no estar presente en otro evento que comparta fecha con el presente evento) y añadir observaciones para cada departamento. Tanto en el caso del personal como en el de material, al pulsar el botón añadir aparecería un popup (o una pantalla) con un buscador para poder encontrar de manera más sencilla al personal necesario (solo saldría el personal correspondiente al departamento que se está editando) y, pulsando sobre el botón “Añadir” de esta nueva pantalla, el empleado o el equipo añadido aparecería en la lista del personal o material del evento. Si pulsa el botón quitar se eliminaría el empleado o el material de la lista correspondiente. Las cuatro primeras pestañas serían iguales (excepto porque cada una mostraría la información correspondiente a su departamento y se añadirían el personal y el material a ese departamento dentro del evento). La última sería diferente y se ve en el siguiente wireframe. El pulsar en el botón “Guardar” se guardaría la información del evento y estaría disponible para los responsables añadidos como personal del evento (cada uno la información de su departamento más la temporalización). Al pulsar en descartar no se guardaría nada y se volvería a la pantalla general de eventos.
>
![](img/Pantalla%20de%20edición%20de%20evento.drawio.png)
## **Pantalla de edición de la temporalización de un evento:** 
Esta es la pantalla que vería el gestor de eventos cuando, dentro de la pantalla de edición de evento pulsase sobre la pestaña de “Temporalización”. Aparecerá una lista con las fases orientativas del evento. A esta información tendrían acceso los responsables de todos los departamentos para poder tener una sincronización eficiente durante el desarrollo del evento (de este modo, los de iluminación y sonido saben que tienen vedado el escenario mientras los de montaje están montado y los de sonido saben que no pueden montar hasta que los de iluminación estén enfocando, por ejemplo). Al pulsar el botón “Añadir fase” se habilitaría una nueva línea en la lista y podría introducir los datos correspondientes a cada columna de la lista.
>
![](img/Pantalla%20de%20edición%20de%20temporalización%20de%20evento.drawio.png)
## **Pantalla de información de evento:** 
Esta pantalla es la que verían los responsables de cada departamento al pulsar sobre uno de los eventos de la pantalla general de eventos. Verían el personal a su cargo en el evento y el material disponible para el mismo. Además, pueden acceder a la pestaña “Temporalización”, en la que pueden ver la lista de fases que el gestor de eventos haya planteado (sería la misma pantalla, pero sin posibilidad de editarla). Pueden añadir observaciones (útiles si en el futuro son sustituidos por otro responsable para conocer los posibles cambios en el montaje o adaptaciones que se hayan hecho con respecto al diseño original) escribiendo en el cuadro para tal efecto y pulsando el botón “añadir”. También pueden descargar los archivos adjuntos que el gestor de eventos haya cargado en el departamento en cuestión pulsando en el botón “Descargar archivos adjuntos”.
>
![](img/Pantalla%20de%20info%20del%20evento.drawio.png)

# Grupos y permisos:
>
- **Comerciales:** Deberán tener permiso para agregar ver los eventos que hay en activo y agregar nuevos eventos.
- **Gestores de eventos:** Deberán tener permisos para ver la lista de eventos en activo y editarlos de cualquier manera (ver al personal disponible en las fechas del evento; agregar personal de iluminación, sonido y montaje; editar horarios; ver listado de material disponible y agregarlo al evento).
- **Responsable de iluminación del evento:** Deberá poder ver la lista de personal de iluminación que tendrá a su cargo en el evento, la lista de material de la que dispondrá, los archivos adjuntos (planos) y los horarios orientativos (fases de montaje, comida, horarios especiales del evento...) así como los horarios fijos (hora de inicio de la función o el evento en sí, hora de llegada, hora de cierre del lugar...)
- **Responsable de sonido del evento:** Deberá poder ver la lista de personal de sonido que tendrá a su cargo en el evento, la lista de material de la que dispondrá, los archivos adjuntos (planos) y los horarios orientativos (fases de montaje, comida, horarios especiales del evento...) así como los horarios fijos (hora de inicio de la función o el evento en sí, hora de llegada, hora de cierre del lugar...)
- **Responsable de montaje del evento:** Deberá poder ver la lista de personal de montaje que tendrá a su cargo en el evento, la lista de material de la que dispondrá y que deberá montar, los archivos adjuntos (planos del lugar y de lo que debe montar) y los horarios orientativos (fases de montaje, comida, horarios especiales del evento, sincronización con los equipos de luces y sonido...) así como los horarios fijos (hora de inicio de la función o el evento en sí, hora de llegada, hora de cierre del lugar...)
- **Almacén:** Deberán tener permiso para ver la lista de material que necesitará cada evento y las fechas de cada uno para poder preparar el equipo para su traslado al iniciar el evento y para su recepción cuando sea devuelto al almacén.

# Diagramas de flujo:
>
**Creaión de evento:**
![](img/creacion%20nuevo%20evento.drawio.png)
>
**Edición de un evento:**
>
![](img/edicion%20nuevo%20evento.drawio.png)
>
**Editar observaciones:**
>
![](img/EDITAR%20OBSERVACIONES.drawio.png)
>
**Descargar archivo:**
>
![](img/DESCARGAR%20ARCHIVO.drawio.png)

# Diagrama E-R versión 1:
>
![](img/ENTIDAD-RELACION.drawio.png)

# Diagrama E-R versión 2:
>
![](img/ENTIDAD-RELACION%202.drawio.png)