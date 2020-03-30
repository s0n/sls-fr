from flask import Flask
#from flask_restplus import Api, Resource
from flask import request
from flask import jsonify
from flask import abort
import base64
import werkzeug
import pprint
import csv
import io
import boto3
from botocore.exceptions import ClientError
import logging

app = Flask(__name__)
@app.route('/convert', methods=['POST'])
def myFunc() :
    if 'file' not in request.files:
        return "passez svp le fichier en paramètre"

    #Chargement du fichier pris en praramètre dans l'Url
    myFile = request.files['file']
    metadata = {}
    data = {}
    data_csv = []
    s3 = boto3.client("s3")
    print(myFile.content_type)

    #Gestion des fichiers TXT
    if myFile.content_type == "text/plain" :
        print(myFile.content_type)
        metadata['nom du fichier'] = myFile.filename
        metadata['type de fichier'] = myFile.content_type
        data['data'] = myFile.read()
        #chargement du fichier dans S3
        try :
            s3.put_object(Body=myFile.stream.read(), Bucket='fil-rouge-aws', Key=myFile.filename)
        except ClientError as e :
            logging.error(e)
        return jsonify(metadonnes = metadata, donnees = data['data'].decode("utf-8"))
        
    #Gestion des fichiers CSV
    elif ((myFile.content_type == "text/csv") or (myFile.content_type == "application/vnd.ms-excel")) :
        metadata['nom du fichier'] = myFile.filename
        metadata['type de fichier'] = myFile.content_type
        with io.TextIOWrapper(myFile) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                data_csv.append(row)
            return jsonify(metadonnes = metadata, donnees = data_csv)

    #Gestion des fichiers PDF
    elif myFile.content_type == 'application/pdf':
        metadata['nom du fichier'] = myFile.filename
        metadata['type de fichier'] = myFile.content_type
        with io.BytesIO(myFile.read()) as pdf_file:
            encoded_string = base64.b64encode(pdf_file.read())
            data['data'] = encoded_string
        s3.put_object(Body=myFile.stream.read(), Bucket='fil-rouge-aws', Key=myFile.filename)
        return jsonify(metadonnes = metadata, donnees = data['data'].decode("utf-8"))
        
    #Gestion des fichiers PNG
    elif myFile.content_type == 'image/png':
        metadata['nom du fichier'] = myFile.filename
        metadata['type de fichier'] = myFile.content_type
        with io.BytesIO(myFile.read()) as png_file:
            encoded_string = base64.b64encode(png_file.read())
            data['data'] = encoded_string
        s3.put_object(Body=myFile.stream.read(), Bucket='fil-rouge-aws', Key=myFile.filename)
        return jsonify(metadonnes = metadata, donnees = data['data'].decode("utf-8"))

    #Default case
    else:
        abort(400, "Fichier non pris en charge")