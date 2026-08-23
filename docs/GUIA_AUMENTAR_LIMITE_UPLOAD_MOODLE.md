# Guía: Aumentar el Límite de Subida de Archivos en Moodle

El archivo de video SCORM (52 MB) supera el límite de subida. Sigue esta guía para aumentarlo.

## ⚠️ Requisitos

**Debes tener acceso de administrador a:**
- Moodle (como administrador)
- Servidor web (acceso FTP/SSH)
- Archivos de configuración de PHP

**Si NO tienes acceso de administrador:** Contacta al administrador del servidor o utiliza soluciones alternativas (compresión de video, YouTube).

---

## 🎯 Nivel 1: Configuración en Moodle (EMPIEZA AQUÍ)

### Paso 1: Verifica el Límite Actual

1. **Accede a Moodle** como administrador.
2. Ve a: **Administración del sitio** → **Seguridad** → **Políticas del sitio**
3. Busca el campo: **Tamaño máximo de los archivos subidos**
4. **Anota el valor** (ej. 16MB, 32MB, 50MB).

### Paso 2: Aumenta el Límite en Moodle

1. En la misma página (**Políticas del sitio**).
2. Campo **"Tamaño máximo de los archivos subidos"**.
3. Selecciona del menú desplegable: **100MB** (o superior).
4. Haz clic en **"Guardar cambios"**.

### Paso 3: Límite a Nivel de Curso

1. Ve a tu curso.
2. **Administración del curso** → **Editar ajustes**
3. Busca: **"Archivos y subidas"** → **Tamaño máximo para archivos cargados**
4. Selecciona: **100MB** (o el máximo disponible).
5. **Guardar y mostrar**.

### ⚠️ Si no ves 100MB como opción...

El límite de Moodle depende del límite PHP establecido en el servidor. Pasa al **Nivel 2**.

---

## 🎯 Nivel 2: Configuración de PHP

El límite de PHP suele ser el verdadero problema. Debes modificar `php.ini`.

### Método A: Acceso a cPanel / Plesk (Hosting Compartido)

**Si tienes cPanel:**

1. Accede a tu **cPanel**.
2. Busca **"Select PHP Version"** o **"MultiPHP INI Editor"**.
3. Selecciona el dominio/carpeta de Moodle.
4. Modifica estos valores:
   ```
   upload_max_filesize = 100M
   post_max_size = 100M
   max_execution_time = 300
   max_input_time = 300
   memory_limit = 256M
   ```
5. **Guarda los cambios**.

**Si tienes Plesk:**

1. Accede a **Plesk**.
2. Ve a **Sitios web y dominios** → tu dominio → **Configuración de PHP**.
3. Modifica:
   ```
   upload_max_filesize = 100M
   post_max_size = 100M
   max_execution_time = 300
   memory_limit = 256M
   ```
4. **Aplicar**.

### Método B: Acceso FTP/SSH (Servidor Dedicado/VPS)

**Encuentra el archivo php.ini:**

```bash
# En Linux, busca php.ini
php -i | grep php.ini

# Rutas comunes:
# /etc/php/7.4/apache2/php.ini
# /etc/php.ini
# /usr/local/etc/php/php.ini
```

**Modifica php.ini:**

1. Abre `php.ini` con un editor (nano, vi, o vía FTP).
2. Busca y modifica estas líneas:

```ini
; ENCUENTRA ESTAS LÍNEAS Y MODIFICA LOS VALORES

upload_max_filesize = 100M
post_max_size = 100M
max_execution_time = 300
max_input_time = 300
memory_limit = 256M
max_file_uploads = 20
```

3. **Guarda el archivo**.
4. **Reinicia el servidor web:**

```bash
# Apache
sudo service apache2 restart
# o
sudo systemctl restart apache2

# Nginx con PHP-FPM
sudo service php7.4-fpm restart
sudo service nginx restart
```

### Método C: Archivo .htaccess (Solo Apache)

Si no tienes acceso a php.ini, intenta crear/modificar el archivo `.htaccess` en la raíz de Moodle:

1. Ve a la carpeta principal de Moodle (vía FTP).
2. Busca el archivo `.htaccess` (podría estar oculto).
3. Abre o crea `.htaccess` y añade:

```apache
# Aumentar límites PHP
php_value upload_max_filesize 100M
php_value post_max_size 100M
php_value max_execution_time 300
php_value max_input_time 300
php_value memory_limit 256M
```

4. **Guarda** e intenta de nuevo.

⚠️ **Nota:** Este método NO siempre funciona (depende de la configuración del servidor).

---

## 🎯 Nivel 3: Verifica los Cambios

### Paso 1: Comprueba la información de PHP

Crea un archivo `phpinfo.php` en la raíz de Moodle:

```php
<?php
phpinfo();
?>
```

Ábrelo en tu navegador: `https://tusitio.com/moodle/phpinfo.php`

Busca estas líneas:
- ✅ `upload_max_filesize` → debe ser ≥ 100M
- ✅ `post_max_size` → debe ser ≥ 100M
- ✅ `max_execution_time` → debe ser ≥ 300
- ✅ `memory_limit` → debe ser ≥ 256M

⚠️ **Elimina phpinfo.php después de comprobarlo** (¡por seguridad!).

### Paso 2: Prueba la Subida

1. Vuelve a Moodle.
2. Ve a **Administración del sitio** → **Seguridad** → **Políticas del sitio**.
3. Comprueba si ahora el menú muestra **100MB** como opción.
4. Si es así, selecciónalo y **guarda**.
5. Intenta subir el archivo de video SCORM (52 MB).

---

## ✅ Solución Rápida (Si No Tienes Acceso)

Si **NO tienes acceso de administrador** al servidor:

### Opción 1: Contacta al Administrador
Envía este correo a tu administrador:

```
Asunto: Solicitud de Aumento de Límite de Subida en Moodle

Estimado administrador,

Necesito subir archivos SCORM de aproximadamente 50-100 MB en el curso de Moodle.
Actualmente el límite es de [X] MB.

¿Podría aumentar los siguientes parámetros en el servidor?

- upload_max_filesize = 100M
- post_max_size = 100M
- max_execution_time = 300
- memory_limit = 256M

¡Muchas gracias!
```

### Opción 2: Comprime el Video

Puedes usar ffmpeg para comprimir el video de 52MB a aproximadamente 15-20MB:

```bash
# Usar ffmpeg para comprimir
ffmpeg -i Demistificare_l_IA.mp4 -vcodec h264 -crf 28 -preset fast Demistificare_l_IA_compressed.mp4
```

### Opción 3: Video Externo (YouTube/Vimeo)

Sube el video a YouTube y crearemos un paquete SCORM muy ligero (< 1MB) que lo incorpore.

---

## 📊 Valores Recomendados para Moodle

| Parámetro | Valor Mínimo | Valor Recomendado |
|-----------|---------------|-------------------|
| `upload_max_filesize` | 64M | 100M - 200M |
| `post_max_size` | 64M | 100M - 200M |
| `max_execution_time` | 300 | 600 |
| `max_input_time` | 300 | 600 |
| `memory_limit` | 128M | 256M - 512M |

---

## 🐛 Resolución de Problemas

### Problema: Los cambios no surten efecto

**Soluciones:**
1. Asegúrate de haber modificado el archivo `php.ini` **correcto** (puede haber varios en el servidor).
2. **Reinicia el servidor web** (Apache/Nginx).
3. **Limpia la caché** de Moodle: Administración → Limpiar todas las cachés.
4. Verifica con `phpinfo()` que los cambios estén activos.

### Problema: Error 500 tras modificar .htaccess

**Solución:**
- El servidor no admite sobrescribir valores de PHP mediante `.htaccess`.
- Elimina las líneas añadidas a `.htaccess`.
- Debes modificar `php.ini` directamente.

### Problema: La subida se bloquea/tiempo de espera agotado

**Solución:**
- Aumenta `max_execution_time` y `max_input_time` a 600 o más.
- Verifica tu conexión a internet (subida lenta).
- Prueba con un archivo más pequeño para verificar.
