# Lección: ¿Qué es SCORM?

SCORM (*Sharable Content Object Reference Model*) es un conjunto de estándares
que permite que un curso funcione en cualquier plataforma LMS compatible.

## ¿Por qué usarlo?

- **Compatibilidad universal**: Moodle, Canvas, TalentLMS, etc.
- **Seguimiento de progreso**: estado de finalización y puntaje.
- **Portabilidad**: un solo archivo `.zip` funciona en cualquier parte.

| Ventaja | Descripción |
|---|---|
| Fiabilidad | Estándar maduro desde 2001 |
| Seguimiento | Soporta cmi.core.lesson_status |

:::apoyo
Este es un dato de apoyo: SCORM 1.2 sigue siendo el estándar más compatible
en 2026, incluso con la existencia de xAPI/cmi5.

VIDEO: https://www.youtube.com/watch?v=dQw4w9WgXcQ
:::

Con esto ya tienes una base para entender el resto del curso.

# Evaluación: Quiz de SCORM

## Pregunta 1

**¿Qué significa la sigla SCORM?**

A) Standard Content Object Reference Model
B) Sharable Content Object Reference Model
C) System Course Object Resource Manager
D) Shared Course Online Resource Model

**Respuesta correcta: B**

**Explicación:** SCORM significa *Sharable Content Object Reference Model*.

---

## Pregunta 2

**¿Cuál es el archivo obligatorio en la raíz de un paquete SCORM?**

A) index.html
B) manifest.json
C) imsmanifest.xml
D) scorm.config

**Respuesta correcta: C**

**Explicación:** El LMS busca `imsmanifest.xml` en la raíz del zip para poder importar el paquete.

# Actividad: Explora tu LMS

Ingresa a tu plataforma LMS (Moodle, Canvas, etc.) y localiza la opción para
subir un "Paquete SCORM". Toma una captura de pantalla del formulario de subida.

:::apoyo
Si no tienes acceso a un LMS, puedes probar el paquete generado abriendo
`index.html` directamente en tu navegador — el modo local funciona sin API SCORM.
:::

# Actividad: Diseña tu primer curso

Escribe el esquema (en 3-4 líneas) de un mini curso de tu elección, indicando:
título, una lección, una evaluación de 2 preguntas y una actividad práctica.

# Enlaces

- [Guía de importación en Moodle](https://docs.moodle.org/en/SCORM_package) - Cómo subir un paquete SCORM en Moodle
- [Especificación ADL SCORM](https://adlnet.gov/projects/scorm/)
