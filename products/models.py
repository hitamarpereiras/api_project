from django.db import models
from io import BytesIO
from PIL import Image
from .myimg import upload_image


class Categoria(models.TextChoices):
        BEBIDAS = 'bebidas', 'bebidas'
        DOCES = 'doces', 'doces'
        SALGADOS = 'salgados', 'salgados'
        PRATOS = 'pratos', 'pratos'
        OUTROS = 'outros', 'outros'

class Produto(models.Model):
    nome = models.CharField(max_length=80, blank=False)
    categoria = models.CharField(
        max_length=40,
        choices=Categoria.choices,
        default=Categoria.BEBIDAS
    )
    descricao = models.TextField(default="Sem descrição", max_length=300)
    preco = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    estoque = models.IntegerField(default=0)
    img_file = models.ImageField(upload_to="temp_uploads", blank=True, null=True) #upload_to="imagens_produtos",
    img_url = models.URLField(max_length=500, blank=True, null=True)
    promocao = models.BooleanField(default=False)
    hora_criacao = models.TimeField(auto_now_add=True)
    data_criacao = models.DateField(auto_now_add=True)
        
    def __str__(self):
        return self.nome[:24] + "..."

    def save(self, *args, **kwargs):
        if self.img_file:
            img = Image.open(self.img_file)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            max_size = (1080, 1080)
            img.thumbnail(max_size)

            buffer = BytesIO()
            img.save(buffer, format="JPEG", quality=95)
            buffer.seek(0)

            # Enviando os bytes diretos
            url_publica = upload_image(buffer.getvalue(), f"{self.nome}.jpg")
            self.img_url = url_publica

            # Apaga a imagem local
            self.img_file.delete(save=False)

        super().save(*args, **kwargs)