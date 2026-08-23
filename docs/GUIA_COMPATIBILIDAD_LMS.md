# Guía de Compatibilidad con Diferentes LMS

Esta guía explica cómo importar los paquetes SCORM 1.2 generados por el sistema en diversas plataformas LMS.

## ¿Qué es SCORM 1.2?

SCORM (Sharable Content Object Reference Model) 1.2 es el estándar de e-learning más utilizado y confiable. Publicado en 2001, es compatible con prácticamente todos los sistemas LMS modernos.

**Ventajas de SCORM 1.2**:
- **Compatibilidad Universal**: Funciona en cualquier LMS que admita SCORM.
- **Fiabilidad**: Estándar maduro y probado durante más de 20 años.
- **Portabilidad**: Un único paquete comprimido funciona en todas las plataformas.
- **Seguimiento**: Monitorea el progreso y el estado de finalización de los estudiantes.
- **Listo para modo local**: Se puede visualizar incluso sin conexión a internet.

---

## Moodle

**Versiones soportadas**: Todas (desde la versión 1.9 en adelante).

### Procedimiento de Importación

1. **Accede al curso** con el rol de profesor o administrador.
2. **Activa el modo de edición**: Haz clic en el botón "Activar edición" en la esquina superior derecha.
3. **Añade una actividad**:
   - Haz clic en **"Añadir una actividad o un recurso"**.
   - Selecciona **"Paquete SCORM"**.
4. **Sube el archivo**:
   - Nombre: Introduce el título del curso.
   - Descripción: (opcional) Describe el contenido.
   - Archivo de paquete: Arrastra y suelta el archivo .zip o utiliza el selector de archivos.
5. **Configura las opciones** (recomendado):
   - Método de calificación: "Calificación más alta".
   - Número de intentos: "Sin límite".
   - Forzar nuevo intento: "Cuando esté completado".
6. **Guardar cambios y mostrar**.

### Problemas Comunes

**La subida falla (archivo demasiado grande)**:
- Aumenta el límite en el archivo `php.ini`: `upload_max_filesize=100M` y `post_max_size=100M`.
- Si utilizas XAMPP: Modifica la configuración mediante el panel de control → Apache Config → PHP (php.ini).
- Reinicia el servicio de Apache después de aplicar las modificaciones.

**El paquete SCORM no se abre**:
- Verifica que el plugin de SCORM esté habilitado en: Administración del sitio → Extensiones → Módulos de actividad.
- Comprueba los permisos del archivo en el servidor: debe ser legible por el servidor web.

---

## Canvas

**Versiones soportadas**: Todas las versiones modernas de Canvas LMS.

### Procedimiento de Importación

1. **Accede al curso** como instructor.
2. **Ve a la Configuración**:
   - Haz clic en **"Configuración"** (Settings) en el menú de navegación del curso.
3. **Importar contenido del curso**:
   - Haz clic en **"Importar contenido del curso"** (Import Course Content).
   - Tipo de contenido: Selecciona **"Paquete SCORM"** (SCORM Package).
4. **Sube el paquete**:
   - Selecciona archivo: Elige tu archivo .zip SCORM.
   - Opciones: Deja la configuración predeterminada o configúrala según tus preferencias.
5. **Importar**: Haz clic en "Importar".
6. **Verificar**: Dirígete a la sección de **"Módulos"** para ver el contenido importado.

### Notas sobre Canvas

- Canvas admite SCORM 1.2 a través del motor SCORM integrado.
- El contenido aparecerá como un módulo o tarea independiente.
- El seguimiento del estado de finalización se sincroniza automáticamente con las calificaciones de Canvas.

---

## Blackboard Learn

**Versiones soportadas**: Blackboard Learn 9.x y superiores.

### Procedimiento de Importación

1. **Accede al curso** como instructor.
2. **Ve a Contenido** (Content):
   - Haz clic en "Contenido" en el menú de navegación.
   - Elige la sección o carpeta donde deseas añadir el SCORM.
3. **Desarrollar contenido**:
   - Haz clic en **"Desarrollar contenido"** (Build Content).
   - Selecciona **"Paquete de contenido (SCORM)"**.
4. **Subir el paquete**:
   - Nombre: Introduce el nombre del curso.
   - Examinar mis archivos: Selecciona el archivo .zip.
   - Opciones: Configura las reglas de seguimiento según tus necesidades.
5. **Enviar** (Submit).

---

## Google Classroom

**Nota importante**: Google Classroom **no es compatible de forma nativa con SCORM**.

### Soluciones Alternativas

**Opción 1 - SCORM Cloud (Recomendada)**:
1. Sube tu paquete SCORM a [SCORM Cloud](https://cloud.scorm.com) (cuenta gratuita con límites).
2. Obtén el enlace para compartir el curso.
3. En Google Classroom:
   - Crea un nuevo "Material" o "Tarea".
   - Añade el enlace obtenido de SCORM Cloud.

**Opción 2 - Conexión Moodle**:
1. Utiliza Moodle como servidor SCORM.
2. Integra Moodle con Google Classroom mediante LTI (Learning Tools Interoperability).

---

## TalentLMS

**Versiones soportadas**: Todas.

### Procedimiento de Importación

1. **Accede al sistema** como administrador o instructor.
2. **Ve al curso**:
   - Haz clic en **"Cursos"**.
   - Selecciona el curso existente o crea uno nuevo.
3. **Añadir contenido**:
   - Haz clic en **"Añadir contenido"**.
   - Selecciona **"SCORM/AICC"**.
4. **Subir**:
   - Haz clic en **"Subir paquete SCORM"**.
   - Selecciona el archivo .zip y espera a que termine la carga.
5. **Configurar y guardar**.

---

## Schoology

**Versiones soportadas**: Todas.

### Procedimiento de Importación

1. **Accede al curso**.
2. **Añadir materiales**:
   - Haz clic en **"Añadir materiales"**.
   - Selecciona **"Añadir archivo/enlace/herramienta externa"**.
3. **Subir SCORM**:
   - Elige **"Archivo"**.
   - Sube tu archivo .zip. Schoology lo detectará automáticamente como un paquete SCORM.
4. **Configura** el título, opciones de entrega y haz clic en **"Guardar"**.

---

## Verificar la Compatibilidad del Paquete

Para comprobar que tu paquete SCORM sea válido antes de subirlo al LMS:

1. **Revisa la estructura del archivo .zip**:
   ```
   paquete.zip
   ├── imsmanifest.xml  (DEBE estar en la raíz)
   ├── index.html
   └── [otros archivos de soporte]
   ```

2. **Valida mediante SCORM Cloud**:
   - Sube el paquete a [https://cloud.scorm.com](https://cloud.scorm.com).
   - Abre el reproductor de pruebas y confirma que el estado de finalización y las llamadas a la API se registren correctamente.

---

## Resolución de Problemas Comunes

### El archivo .zip no se reconoce como un paquete SCORM válido
- **Causa**: El archivo `imsmanifest.xml` no se encuentra en el directorio raíz del archivo zip.
- **Solución**: Descomprime el archivo, asegúrate de que `imsmanifest.xml` esté en la carpeta raíz y vuelve a comprimir el contenido directamente (evitando meterlo en una carpeta contenedora al comprimir).

### El curso se abre pero no guarda el progreso
- **Causa**: Problemas con la comunicación del script de la API SCORM.
- **Soluciones**:
  - Asegúrate de que el LMS esté configurado para soportar SCORM 1.2.
  - Verifica en el navegador que los bloqueadores de ventanas emergentes (pop-ups) no estén interfiriendo.
  - Pulsa F12 para revisar si hay errores de JavaScript en la consola.

---

## Buenas Prácticas

1. **Prueba siempre antes de publicar**: Valida tu paquete en SCORM Cloud.
2. **Optimiza el tamaño de los archivos**: Mantén los videos por debajo de 50 MB y los audios por debajo de 10 MB si se incluyen de forma local.
3. **Diseño Web Estándar**: Asegúrate de que el diseño sea responsivo y no utilice tecnologías obsoletas.
