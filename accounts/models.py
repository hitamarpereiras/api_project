from django.contrib.auth.models import AbstractUser
from django.db import models
from io import BytesIO
from PIL import Image
from django.utils import timezone
from .myimg import upload_image

def current_date():
    return timezone.localdate()

def current_time():
    return timezone.localtime().time()

class User(AbstractUser):
    is_company = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class EmpresaPerfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nome_empresa = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.TextField(blank=True, null=True)
    telefone = models.CharField(max_length=20)
    img_file = models.ImageField(upload_to="temp_uploads", blank=True, null=True)
    img_url = models.URLField(max_length=500, blank=True, null=True)
    data_criacao = models.DateField(default=current_date)
    hora_criacao = models.TimeField(default=current_time)

    def __str__(self):
        return self.nome_empresa
    
    """Salava a imagem no banco de dados"""
    def save(self, *args, **kwargs):
        if self.img_file:
            img = Image.open(self.img_file)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            max_size = (512, 512)
            img.resize(max_size)

            buffer = BytesIO()
            img.save(buffer, format="JPEG", quality=95)
            buffer.seek(0)

            # Enviando os bytes diretos
            url_publica = upload_image(buffer.getvalue(), f"{self.cnpj}.jpg")
            self.img_url = url_publica

            # Apaga a imagem local
            self.img_file.delete(save=False)

        super().save(*args, **kwargs)

class EmpresaInfo(models.Model):
    id_empresa = models.OneToOneField(
        EmpresaPerfil, 
        on_delete=models.CASCADE, 
        related_name="empresa_info"
    )

    total_vendas_dia = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    total_vendas_mes = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    total_vendas_ano = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    total_vendas = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    ultimo_acesso = models.DateField(default=current_date)
    data_criacao = models.DateField(default=current_date)
    hora_criacao = models.TimeField(default=current_time)

    def __str__(self):
        return f"Informações da {self.id_empresa}"

