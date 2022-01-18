Fil rouge Serverless

## Procédure Test :
l'application est déjà déployée en serverless dans mon compte aws
### Faire une requête : 
  `curl -X POST "https://4njqppxehl.execute-api.eu-west-1.amazonaws.com/dev/convert" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@{lien vers le fichier a uploader}" ` en remplaçant {lien vers le fichier a uploader} par le chemin vers le fichier à envoyer.

## Installation dans votre instance personelle
### 1- clonez le projet
`git clone https://github.com/s0n/sls-fr.git`
### 2- installez serverless
`$ npm install --save-dev serverless-wsgi serverless-python-requirements`
#### Serverless a besoin d'accéder à votre compte pour cela il faut définir vos credentials
`export AWS_ACCESS_KEY_ID=<your-key-here`


`export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>`
### 3- Activez l'environnement virtuel
`source venv/bin/activate`


il faut au préalable avoir installé virtualenv (`pip install virtualenv`)
### 4- déployez l'application dans votre compte aws
avec la commande `sls depoy`
### 5- faites des requêtes vers l'application déployée
cf. Procédure de test


ngbangoAgent3: j7MvgjbIEk)p-V6vdX2ama$!IeNL(6@K
