# ⚡ Qwen Inferencia On-Cloud con Google Colab Pro

Repositorio listo para desplegar inferencia rápida de la familia **Qwen 2.5** (modelos generales y **Qwen2.5-Coder**) en GPUs de **Google Colab Pro**, exponiendo una API pública compatible con OpenAI y una interfaz web con 1 solo clic.

---

## 🚀 Acceso Rápido (1 Clic)

Haz clic en cualquiera de los botones para abrir el notebook directamente en Google Colab:

| Opción | Motor | Descripción | Enlace |
| :--- | :--- | :--- | :--- |
| **Opción A (Recomendada)** | **vLLM** | Máximo rendimiento (PagedAttention), streaming ultra rápido, compatible con API de OpenAI y Chat Gradio integrado. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TU_USUARIO/TU_REPO/blob/main/notebooks/qwen_vllm_inference.ipynb) |
| **Opción B** | **Ollama** | Ecosistema Ollama clásico con CLI (`ollama run/pull`) y túnel público. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TU_USUARIO/TU_REPO/blob/main/notebooks/qwen_ollama_inference.ipynb) |

> 💡 **Nota**: Sustituye `TU_USUARIO/TU_REPO` por tu usuario y nombre de repositorio en GitHub.

---

## 🎯 ¿Qué permite este setup?

1. **Aprovechar las GPUs de Colab Pro**: Utiliza GPUs de nivel servidor (**NVIDIA A100**, **L4** o **T4**) para ejecutar modelos de 7B, 14B o 32B sin consumir recursos de tu ordenador local.
2. **Endpoint Público Gratuito (Cloudflare Tunnel)**: Sin necesidad de crear cuentas en ngrok ni configurar routers; genera una URL segura `https://xxxx.trycloudflare.com/v1`.
3. **Compatibilidad Total con OpenAI**: Conecta cualquier cliente local (Cursor, VS Code con Continue, LibreChat, Open WebUI, LangChain, LlamaIndex o scripts de Python).
4. **Web UI Inmediata**: Incluye interfaz gráfica de chat con **Gradio** en el propio Colab o con enlace público compartible.

---

## 🧠 Guía de VRAM y Modelos en Colab Pro

Según la GPU que selecciones en Colab (*Entorno de ejecución > Cambiar tipo de entorno de ejecución*):

| GPU en Colab | VRAM Disponible | Modelos Recomendados |
| :--- | :--- | :--- |
| **T4** (Básica) | ~15-16 GB | • `Qwen/Qwen2.5-7B-Instruct`<br>• `Qwen/Qwen2.5-Coder-7B-Instruct`<br>• `Qwen/Qwen2.5-14B-Instruct-AWQ` *(contexto 4k)* |
| **L4** (Recomendada Colab Pro) | ~22-24 GB | • `Qwen/Qwen2.5-7B-Instruct` *(velocidad extrema)*<br>• `Qwen/Qwen2.5-14B-Instruct-AWQ`<br>• `Qwen/Qwen2.5-Coder-14B-Instruct-AWQ` |
| **A100** (Premium Colab Pro) | ~40 GB / 80 GB | • `Qwen/Qwen2.5-14B-Instruct` (FP16/BF16)<br>• `Qwen/Qwen2.5-32B-Instruct-AWQ`<br>• `Qwen/Qwen2.5-Coder-32B-Instruct-AWQ`<br>• `Qwen/Qwen2.5-72B-Instruct-AWQ` *(en A100 80GB)* |

---

## 📁 Estructura del Proyecto

```text
.
├── notebooks/
│   ├── qwen_vllm_inference.ipynb    # Servidor de producción vLLM + Gradio
│   └── qwen_ollama_inference.ipynb  # Servidor alternativo con Ollama
├── client_test.py                   # Script local para probar la inferencia desde tu Mac/PC
├── .env.example                     # Variables de entorno de ejemplo
└── README.md                        # Documentación e inicio rápido
```

---

## 🛠️ Cómo Subir este Proyecto a tu GitHub

Para tenerlo disponible siempre y abrirlo con 1 clic:

1. **Inicializa el repositorio y haz el primer commit**:
   ```bash
   cd 0017-QwenColab
   git init
   git add .
   git commit -m "feat: setup inicial de inferencia qwen en colab con vllm y ollama"
   ```

2. **Crea un repositorio en GitHub** (público para que Colab pueda leer los notebooks).

3. **Vincula y sube tu código**:
   ```bash
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
   git push -u origin main
   ```

4. **Actualiza los badges de este README**:
   Reemplaza `TU_USUARIO/TU_REPO` en los enlaces de la tabla de arriba con tu usuario y repositorio.

---

## 💻 Conectar desde tu Máquina Local (Mac / PC)

Una vez ejecutada la celda del notebook en Colab, verás en la salida algo como:

```text
=================================================================
🎉 ¡TÚNEL PÚBLICO ACTIVADO CON ÉXITO!
🌐 Base URL: https://alpha-beta-gamma.trycloudflare.com/v1
🔑 API Key: colab-qwen-secret
🤖 Model ID: Qwen/Qwen2.5-Coder-7B-Instruct
=================================================================
```

### 1. Probar con el script de Python (`client_test.py`)

Instala las dependencias locales:
```bash
pip install openai
```

Ejecuta una petición de prueba con streaming:
```bash
python3 client_test.py --url "https://alpha-beta-gamma.trycloudflare.com/v1" --key "colab-qwen-secret"
```

### 2. Conectar a Cursor o VS Code (Continue)

En tu extensión o herramienta de IA local (por ejemplo **Continue.dev** en VS Code o la configuración de OpenAI API en **Cursor**):

- **Provider**: OpenAI
- **Base URL**: `https://tu-url-de-cloudflare.trycloudflare.com/v1`
- **API Key**: `colab-qwen-secret` (o la que hayas configurado en el notebook)
- **Model Name**: `Qwen/Qwen2.5-Coder-7B-Instruct` (o el modelo que hayas arrancado)

### 3. Conectar mediante `curl`

```bash
curl https://tu-url-de-cloudflare.trycloudflare.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer colab-qwen-secret" \
  -d '{
    "model": "Qwen/Qwen2.5-Coder-7B-Instruct",
    "messages": [{"role": "user", "content": "Hola Qwen, ¿cómo estás?"}],
    "temperature": 0.7
  }'
```

---

## 💡 Consejos para Google Colab Pro

- **Tiempo de ejecución en segundo plano**: En Colab Pro puedes activar la casilla de ejecución en segundo plano en la configuración del notebook para que no se detenga al cerrar la pestaña.
- **Descargas rápidas**: Colab tiene un ancho de banda de red muy elevado (>1 Gbps), por lo que descargar un modelo de 7B o 14B suele tardar menos de 60-90 segundos.
- **Cuantización AWQ**: Para modelos grandes (14B y 32B), usa las versiones `-AWQ`. Ocupan la mitad de VRAM manteniendo prácticamente el 99% de la calidad original.
