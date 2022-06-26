# NewCombin


`Proyecto creado como test. se utilizó Django rest framework para la creación de APIS, asi como tambien python-barcode y pillow para generar imagenes de códigos de barra`

# Instalación

##### 1) Clonar o descargar el proyecto del repositorio

`git clone https://github.com/ildecarz/NewCombin.git`

##### 2) Crear un entorno virtual para posteriormente instalar las librerias del proyecto

- `python3 -m venv venv` (Windows)
-  `virtualenv venv -p python3` (Linux)

##### 3) Activar el entorno virtual de nuestro proyecto

- `cd venv\Scripts\activate.bat` (Windows)
- `source venv/bin/active` (Linux)

##### 4) Instalar todas las librerias del proyecto que se encuentran en requirements.txt

- `pip install -r requirements.txt`

##### 5) Crear la base de datos con las migraciones y el superuser para iniciar sesión

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`


##### 6) Para acceder a los diferentes endpoints de la app

- `python manage.py runserver`

- `Ingresar a la url localhost:8000/admin con el superusuario creado podra acceder al panel admin`

- `Ingresar a la url localhost:8000/api/create-tax/ para crear una nueva boleta`

- `Ingresar a la url localhost:8000/api/pay-tax/ para crear un nuevo pago`

- `Ingresar a la url localhost:8000/api/payables/ para listar los pagos creados y filtrarlos por status y servicio`


##### 7)  NOTA: Aunque no se solicitó, se crearon test sencillos para mejorar la performance del proyecto