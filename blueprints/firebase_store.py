from flask import Flask, request, jsonify, Blueprint
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud import storage
import base64
import re
import uuid


# Rota para listar clientes
firebase_store_blueprint = Blueprint('firebase_store', __name__)


# --------------------------------
# ---------------------------------
# Inicialize o Firebase Admin
cred = credentials.Certificate('./zoomb-os-firebase.json')
firebase_admin.initialize_app(cred, {'storagBucket': 'zoomb-os.appspot.com'})

# Inicialize o Firestore
db = firestore.client()

# Inicialize o Firebase Storage
storage_client = storage.Client.from_service_account_json(
    'zoomb-os-firebase.json')
bucket_name = 'gs://zoomb-os.appspot.com'
bucket = storage_client.bucket(bucket_name)

# --------------------------------
# ---------------------------------


@firebase_store_blueprint.route('/Gravar_imagem', methods=['POST'])
def Gravar_imagem():
    data = request.get_json()
    image_data = data['image']

    # Remova o prefixo 'data:image/png;base64,'
    image_data = re.sub('^data:image/.+;base64,', '', image_data)

    # Decodifique a imagem
    image_data = base64.b64decode(image_data)

    # Crie um nome único para o arquivo
    file_name = f'signatures/{uuid.uuid4()}.png'

    # Carregue a imagem no Firebase Storage
    blob = bucket.blob(file_name)
    blob.upload_from_string(image_data, content_type='image/png')

    # Obtenha a URL pública da imagem
    image_url = blob.public_url

    # Salve a URL no Firestore
    doc_ref = db.collection('signatures').document()
    doc_ref.set({
        'signature_url': image_url
    })
    # Retorne a URL da assinatura como uma resposta JSON
    return jsonify({'status': 'success', 'url': image_url}), 200
