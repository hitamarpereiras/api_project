from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmpresaCreateSerializer
from .models import EmpresaPerfil, EmpresaInfo
from .serializers import SerializerEmpresa, EmpresaCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model

User = get_user_model()

class EmpresaView(APIView):
    """
    GET -> retorna os dados da empresa autenticada (com EmpresaInfo)
    POST -> cria novo usuário + empresa + empresaInfo
    """
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]  # cadastro público
        return [IsAuthenticated()]  # GET requer login

    def get(self, request):
        try:
            empresa = EmpresaPerfil.objects.get(user=request.user)
        except EmpresaPerfil.DoesNotExist:
            return Response({"error": "Empresa não encontrada"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SerializerEmpresa(empresa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            serializer = EmpresaCreateSerializer(data=request.data)

            if serializer.is_valid():
                empresa = serializer.save()

                # cria EmpresaInfo vinculada automaticamente
                EmpresaInfo.objects.create(
                    id_empresa=empresa,
                    total_vendas_dia=0,
                    total_vendas_mes=0,
                    total_vendas_ano=0,
                    total_vendas=0
                )

                return Response(
                    {
                        "message": "Empresa criada com sucesso!",
                        "empresa": SerializerEmpresa(empresa).data
                    },
                    status=status.HTTP_201_CREATED
                )

        except Exception as err:
            return Response({"err views": str(err)}, status=status.HTTP_400_BAD_REQUEST)
