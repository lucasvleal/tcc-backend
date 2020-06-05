import os
from flask import Flask, jsonify, request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from cloudinary.templatetags import cloudinary

from .serializer import ImageSerializer
from .models import Imagens

app = Flask(__name__)

parser_classes = (MultiPartParser, FormParser,)
serializer_class = ImageSerializer

@app.route('/images')
def get(self, request, format=None):
    imagens = Imagens.objects.all()
    serializer = ImageSerializer(imagens, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

def post(self, request, format=None):
	serializer = self.serializer_class(data=request.data)
	if serializer.is_valid():
	    serializer.save()
	    return Response(serializer.data, status=status.HTTP_201_CREATED)
	else:
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @app.route('/')
# def nao_entre_em_panico():
#     if request.headers.get('Authorization') == '42':
#         return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
#     return jsonify({"message": "Não entre em pânico!"})

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)
