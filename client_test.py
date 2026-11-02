#!/usr/bin/env python3
"""
client_test.py
Script local para probar la inferencia de tu servidor Qwen corriendo en Google Colab.

Requisitos:
    pip install openai python-dotenv

Uso:
    python3 client_test.py --url "https://tu-subdominio.trycloudflare.com/v1" --key "colab-qwen-secret"
"""

import argparse
import sys
import os
from openai import OpenAI


def parse_args():
    parser = argparse.ArgumentParser(description="Prueba tu endpoint de Qwen en Google Colab")
    parser.add_argument(
        "--url",
        type=str,
        default=os.environ.get("OPENAI_BASE_URL", "http://localhost:8000/v1"),
        help="Base URL del servidor (ej: https://xxxx.trycloudflare.com/v1)",
    )
    parser.add_argument(
        "--key",
        type=str,
        default=os.environ.get("OPENAI_API_KEY", "colab-qwen-secret"),
        help="API Key configurada en el notebook (o 'ollama' para Ollama)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="Qwen/Qwen2.5-Coder-7B-Instruct",
        help="Nombre del modelo a solicitar",
    )
    parser.add_argument(
        "--prompt",
        type=str,
        default="Escribe una función en Python para calcular el factorial de un número con memoización y tipado estático.",
        help="Prompt a enviar",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    print(f"📡 Conectando a: {args.url}")
    print(f"🤖 Modelo solicitado: {args.model}")
    print(f"📝 Prompt: {args.prompt}\n")
    print("=" * 60)
    print("Respuesta (Streaming):")
    print("=" * 60)

    try:
        client = OpenAI(base_url=args.url, api_key=args.key)

        # Si no sabemos el modelo exacto, podemos listar los disponibles
        try:
            models_response = client.models.list()
            available_models = [m.id for m in models_response.data]
            if available_models:
                print(f"ℹ️ Modelos detectados en el servidor: {available_models}")
                # Usar el primero si el especificado no coincide
                if args.model not in available_models:
                    print(f"⚠️ Cambiando modelo a: {available_models[0]}")
                    args.model = available_models[0]
        except Exception:
            pass  # Algunos servidores o túneles pueden no implementar models.list()

        stream = client.chat.completions.create(
            model=args.model,
            messages=[
                {"role": "system", "content": "Eres un asistente de programación experto, claro y conciso."},
                {"role": "user", "content": args.prompt},
            ],
            temperature=0.7,
            max_tokens=1024,
            stream=True,
        )

        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)

        print("\n\n" + "=" * 60)
        print("✅ Inferencia completada con éxito.")

    except Exception as e:
        print(f"\n❌ Error al conectar con el servidor: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
