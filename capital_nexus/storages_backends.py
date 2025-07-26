import os
from django.core.files.storage import Storage
from supabase import create_client
from django.core.files.base import ContentFile
from django.conf import settings

class SupabaseStorage(Storage):
    def __init__(self):
        self.url = settings.SUPABASE_URL
        self.key = settings.SUPABASE_KEY
        self.bucket_name = settings.SUPABASE_BUCKET_NAME
        self.client = create_client(self.url, self.key)
        self.bucket = self.client.storage.from_(self.bucket_name)

    def _save(self, name, content):
        self.bucket.upload(name, content, {"cacheControl": "3600", "upsert": True})
        return name

    def exists(self, name):
        try:
            res = self.bucket.list()
            return any(f["name"] == name for f in res["data"])
        except Exception:
            return False

    def url(self, name):
        return self.bucket.get_public_url(name)

    def delete(self, name):
        self.bucket.remove([name])

    def open(self, name, mode="rb"):
        res = self.bucket.download(name)
        return ContentFile(res)

    def size(self, name):
        # Supabase não fornece diretamente o tamanho do arquivo
        return None
