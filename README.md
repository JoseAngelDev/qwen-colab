# ⚡ Qwen 3.8 & GLM Inferencia On-Cloud con Google Colab Pro

Repositorio listo para desplegar inferencia rápida de modelos de última generación y sin censura (**Abliterated / Cybersecurity**) como **Huihui-Qwen3.8-27B**, **SC117 Qwen3.8 Flash-Next** y **GLM-5.3** en GPUs de **Google Colab Pro**, exponiendo una API pública compatible con OpenAI y una interfaz web con 1 solo clic.

---

## 🚀 Acceso Rápido (1 Clic)

Haz clic en cualquiera de los botones para abrir el notebook directamente en Google Colab:

| Opción | Motor | Modelos Preconfigurados | Enlace |
| :--- | :--- | :--- | :--- |
| **Opción A (Recomendada)** | **vLLM** | • `huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF`<br>• `SC117/Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF`<br>• `dealignai/GLM-5.3-CYBERSECURITY-FP8` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JoseAngelDev/qwen-colab/blob/main/notebooks/qwen_vllm_inference.ipynb) |
| **Opción B** | **Ollama** | • `hf.co/huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF:Q4_K`<br>• `hf.co/SC117/Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF:Q2_0` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JoseAngelDev/qwen-colab/blob/main/notebooks/qwen_ollama_inference.ipynb) |

> 💡 **Nota**: Los botones están vinculados al repositorio `JoseAngelDev/qwen-colab`.

---

## 🎯 ¿Qué permite este setup?

1. **Modelos Modernos Abliterated y de Ciberseguridad**: Diseñado para correr `Qwen3.8 27B` y variantes afinadas por la comunidad.
2. **Aprovechar GPUs de Colab Pro**: Utiliza GPUs de nivel servidor (**NVIDIA A100** o **L4**) para mover modelos de 27B parámetros con fluidez.
3. **Endpoint Público Gratuito (Cloudflare Tunnel)**: Genera una URL segura `https://xxxx.trycloudflare.com/v1` lista para conectar a Cursor, VS Code, LibreChat o Python.
4. **Web UI Inmediata**: Incluye interfaz de chat con **Gradio** en el propio Colab o con enlace compartible.

---

## 🧠 Compatibilidad de Modelos en Colab Pro

| Modelo | Formato | VRAM Requerida | GPU Recomendada en Colab | Notas |
| :--- | :--- | :--- | :--- | :--- |
| **Huihui-Qwen3.8-27B-abliterated** | GGUF (`Q4_K`) | ~16-17 GB | **L4 (24 GB)** o **A100 (40 GB)** | 🏆 **Mejor equilibrio** inteligencia / velocidad sin censura. |
| **SC117/Qwen3.8-Flash-Next** | GGUF (`Q2_0` / `IQ3`) | ~6-10 GB | **T4 (16 GB)** o **L4 (24 GB)** | ⚡ Inferencia ultra rápida y bajo consumo de VRAM. |
| **dealignai/GLM-5.3-CYBERSECURITY** | Safetensors FP8 | >80 GB | **A100 (80 GB)** | 🛡️ MoE masivo de ciberseguridad (requiere cluster/A100 80GB). |

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
🤖 Model ID: huihui-ai/Huihui-Qwen3.8-27B-abliterated
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
- **Model Name**: `huihui-ai/Huihui-Qwen3.8-27B-abliterated` (o el modelo que hayas arrancado)

### 3. Conectar mediante `curl`

```bash
curl https://tu-url-de-cloudflare.trycloudflare.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer colab-qwen-secret" \
  -d '{
    "model": "huihui-ai/Huihui-Qwen3.8-27B-abliterated",
    "messages": [{"role": "user", "content": "Hola, ¿cómo estás?"}],
    "temperature": 0.7
  }'
```

---

## 💡 Consejos para Google Colab Pro

- **Tiempo de ejecución en segundo plano**: En Colab Pro puedes activar la casilla de ejecución en segundo plano en la configuración del notebook para que no se detenga al cerrar la pestaña.
- **Descargas rápidas**: Colab tiene un ancho de banda de red muy elevado (>1 Gbps), por lo que descargar un modelo de 7B o 14B suele tardar menos de 60-90 segundos.
- **Cuantización AWQ**: Para modelos grandes (14B y 32B), usa las versiones `-AWQ`. Ocupan la mitad de VRAM manteniendo prácticamente el 99% de la calidad original.
