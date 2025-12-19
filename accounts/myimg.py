from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime
import os
import uuid

url= str("https://vastxqzdhjxfgobkkxcp.supabase.co")
key= str("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZhc3R4cXpkaGp4ZmdvYmtreGNwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE5NDEzNzAsImV4cCI6MjA3NzUxNzM3MH0.TRDZH8UF1R1FBOAkLiXp4byWgolWRLD36uai-J9B1sE")

supabase = create_client(url, key)

def upload_image(file_bytes, filename):
    SUPABASE_BUCKET = "imagens_empresa"

    date = datetime.now().strftime("%d%m%Y_%H%M%S")
    ext = filename.split('.')[-1]
    name_image = f"img_{uuid.uuid4().hex[:10]}{date}.{ext}"
    path_storage = f"public/{name_image}"

    # bytes diretos (sem BytesIO)
    response = supabase.storage.from_(SUPABASE_BUCKET).upload(
        path_storage,
        file_bytes,  # <-- aqui vão os bytes crus
        file_options={"content-type": f"image/{ext}"}
    )

    # O SDK retorna None quando sucesso precisamos conferir erros
    if hasattr(response, "error") and response.error is not None:
        raise Exception(response.error.message)

    # Gera URL pública
    url_publica = supabase.storage.from_(SUPABASE_BUCKET).get_public_url(path_storage)
    return url_publica

def upload_image_colaborator(file_bytes, filename):
    SUPABASE_BUCKET = "imagens_colaboradores"

    date = datetime.now().strftime("%d%m%Y_%H%M%S")
    ext = filename.split('.')[-1]
    name_image = f"{uuid.uuid4().hex[:10]}_{date}.{ext}"
    path_storage = f"public/{name_image}"

    # bytes diretos (sem BytesIO)
    response = supabase.storage.from_(SUPABASE_BUCKET).upload(
        path_storage,
        file_bytes,  # <-- aqui vão os bytes crus
        file_options={"content-type": f"image/{ext}"}
    )

    # O SDK retorna None quando sucesso precisamos conferir erros
    if hasattr(response, "error") and response.error is not None:
        raise Exception(response.error.message)

    # Gera URL pública
    url_publica = supabase.storage.from_(SUPABASE_BUCKET).get_public_url(path_storage)
    return url_publica