from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import EmpresaPerfil, EmpresaInfo

User = get_user_model()

class EmpresaCreateSerializer(serializers.ModelSerializer):
    # Campos do User
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = EmpresaPerfil
        fields = [
            "username",
            "password",
            "cnpj",
            "nome_empresa",
            "endereco",
            "telefone",
            "img_file"
        ]

    def create(self, validated_data):
        username = validated_data.pop("username")
        password = validated_data.pop("password")

        # Criar o usuário
        user = User.objects.create_user(
            username=username,
            password=password,
            is_company=True
        )

        # Criar perfil da empresa
        empresa = EmpresaPerfil.objects.create(
            user=user,
            **validated_data
        )

        # Criar EmpresaInfo vinculada (com valores padrão)
        EmpresaInfo.objects.create(
            id_empresa=empresa,
            total_vendas_dia=0,
            total_vendas_mes=0,
            total_vendas_ano=0,
            total_vendas=0
        )

        return empresa
    
class SerializerEmpresaInfo(serializers.ModelSerializer):
    class Meta:
        model = EmpresaInfo
        fields = '__all__'

class SerializerEmpresa(serializers.ModelSerializer):
    empresa_info = SerializerEmpresaInfo(read_only=True)

    class Meta:
        model = EmpresaPerfil
        fields = '__all__'
        read_only_fields = []