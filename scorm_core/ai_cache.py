import hashlib
import json
import os
from pathlib import Path
from typing import Any, Callable

CACHE_DIR = Path(".cache/ai")


def obtener_hash_cache(namespace_o_prompt: str, prompt_o_contenido: str = "", params_o_modelo: Any = "") -> str:
    """Genera una clave SHA-256 única y determinista para los parámetros y contenido de la llamada."""
    raw_params = json.dumps(params_o_modelo, sort_keys=True) if isinstance(params_o_modelo, (dict, list)) else str(params_o_modelo)
    raw = f"{namespace_o_prompt}___{prompt_o_contenido}___{raw_params}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def cache_ai_call(
    namespace_o_prompt: str,
    prompt_o_contenido: str,
    generator_or_params: Any,
    call_fn: Callable[[], Any] | None = None,
    modelo: str = "",
    force_refresh: bool = False,
    cache_dir: Path | None = None
) -> Any:
    """
    Ejecuta una llamada de generación con IA intermediada por caché en disco.
    
    Soporta dos firmas:
    1) cache_ai_call(namespace, prompt, params_dict, callable)
    2) cache_ai_call(prompt, contenido, callable, modelo=...)
    """
    if callable(generator_or_params):
        generator_fn = generator_or_params
        params = modelo
    elif callable(call_fn):
        generator_fn = call_fn
        params = generator_or_params
    else:
        raise ValueError("Se debe proporcionar una función generadora callable a cache_ai_call.")

    if os.getenv("EDUCAI_NO_CACHE", "").lower() in ("1", "true", "yes"):
        force_refresh = True

    base_dir = cache_dir or CACHE_DIR
    cache_key = obtener_hash_cache(namespace_o_prompt, prompt_o_contenido, params)
    cache_file = base_dir / f"{cache_key}.json"

    if not force_refresh and cache_file.exists():
        try:
            cached_data = json.loads(cache_file.read_text(encoding="utf-8"))
            print(f"[CACHE HIT] Respuesta de IA recuperada de cache ({cache_key[:10]}...) - 0 tokens usados.")
            return cached_data
        except Exception as e:
            print(f"[CACHE WARN] No se pudo leer archivo de caché {cache_file.name}: {e}. Re-generando...")

    # Ejecutar llamada real a la IA
    resultado = generator_fn()

    # Guardar en caché
    try:
        base_dir.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[CACHE STORE] Respuesta de IA guardada en cache ({cache_key[:10]}...).")
    except Exception as e:
        print(f"[CACHE WARN] No se pudo escribir en caché: {e}")

    return resultado
