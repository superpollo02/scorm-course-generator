# Guía para Importar Cursos en Moodle

## ⚠️ Solución Recomendada: Importar en un Curso Existente

Si recibes el error `restore_unknown_restore_type`, utiliza este método alternativo:

### Paso 1: Crea un Curso Vacío

1. **Accede a Moodle** como administrador o profesor con permisos de edición.
2. **Ve a:**
   - Administración del sitio → Cursos → Administrar cursos y categorías.
3. **Crea un nuevo curso:**
   - Haz clic en **"Crear nuevo curso"**.
4. **Completa los detalles:**
   - **Nombre completo**: `Introducción a la Inteligencia Artificial para Principiantes`
   - **Nombre corto**: `IA-Principiantes-2024`
   - **Categoría**: Selecciona o crea una categoría (ej. "Tecnología" o "IA").
   - **Formato de curso**: **Temas** (o Semanal).
   - **Número de secciones**: **10**.
   - **Fecha de inicio**: Selecciona la fecha deseada.
5. **Guardar cambios y mostrar**.

### Paso 2: Restaura la Copia de Seguridad en el Curso

1. **Entra al curso** que acabas de crear.
2. **Ve a:**
   - Icono de configuración (⚙️) en la esquina superior derecha (o menú de navegación del curso) → **"Restaurar"**.
3. **Sube el archivo:**
   - Haz clic en "Seleccionar un archivo".
   - Elige **`AI-Principianti-FIXED.mbz`**.
   - Haz clic en "Restaurar".
4. **Confirmar:**
   - Revisa la información de los componentes que se van a restaurar.
   - Haz clic en **"Continuar"**.
5. **Destino:**
   - Selecciona **"Fusionar la copia de seguridad con este curso"** o bien **"Borrar el contenido del curso actual y después restaurar"** (se recomienda esta última opción si el curso está vacío).
   - Haz clic en "Continuar".
6. **Ajustes:**
   - Asegúrate de marcar:
     - ✅ Incluir actividades y recursos.
     - ✅ Incluir bloques.
   - Haz clic en "Siguiente".
7. **Esquema:**
   - Revisa los elementos específicos que se van a restaurar.
   - Haz clic en **"Ejecutar restauración"**.
8. **Finalizar:**
   - Espera a que se complete el proceso (suele tardar de 30 a 90 segundos).
   - Haz clic en "Continuar".
   - ¡Tu curso ya está listo y restaurado!

---

## 🔄 Método Alternativo: Importación Directa

Si tu versión de Moodle lo permite, puedes utilizar la importación directa:

1. **Crea el curso vacío** (siguiendo las instrucciones del Paso 1).
2. **Entra en el curso**.
3. **Ve a:**
   - Configuración → **"Importar"**.
4. **Sube el archivo** `AI-Principianti-FIXED.mbz` directamente o selecciona las actividades del curso que deseas copiar.

---

## 📋 Método Manual (Plan de Reserva)

Si los métodos anteriores fallan, puedes construir el contenido de forma manual:

### 1. Utiliza el Archivo Markdown
Utiliza el archivo `course-content-edited.md` que contiene todo el texto del curso estructurado.

### 2. Crea las Secciones Manualmente
Para cada módulo (1 al 10):
1. **Añade una sección** en Moodle.
2. Copia el **Título de la sección** desde el archivo Markdown.
3. Haz clic en **"Añadir una actividad o recurso"**:
   - Para textos explicativos y teoría → Añade una **"Página"**.
   - Para ejercicios o entregas → Añade una **"Tarea"**.
   - Para debates → Añade un **"Foro"**.
   - Para evaluaciones → Añade un **"Cuestionario"**.

### 3. Copia el Contenido
- Abre `course-content-edited.md` en tu editor de texto.
- Copia y pega la información correspondiente en los campos de descripción o contenido de las actividades de Moodle. Moodle adaptará el formato markdown a HTML de manera automática.

---

## 🛠️ Resolución de Problemas

### Errore: "restore_unknown_restore_type"
- **Solución**: Utiliza el método de fusionar y restaurar en un curso existente descrito en el Paso 1 de esta guía.

### Error: "Invalid backup file"
- **Solución**: Comprueba que el archivo `.mbz` no se haya corrompido durante la descarga y vuélvelo a intentar.

### Los caracteres especiales en español no se ven bien
- **Solución**: Asegúrate de que el idioma de tu sitio Moodle y de la base de datos esté configurado en codificación UTF-8.
