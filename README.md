# flask-shopy-2687386
# # DOCUMENTACIÓN
- Comandos: 
- - pip install flask flask-migrate flask-sqlalchemy mysql-client
- - pip install pymysql
- Después de instalar las dependencias anteriores ejecutar;
- - flask db init
- - flask db migrate
- - flask db upgrade
- Errores comunes:
- - Cuando sale 
- - "INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
ERROR [flask_migrate] Error: Can't locate revision identified by '9dc9bf37dd01'"
- - Se debe eliminar la base de datos desde el MySQL y crearla de nuevo, despues, ejecutar de nuevo el migrte y upgrade
# # CONSEJOS
- Al hacer un cambio en los modelos hacer migrate y posteriormente, hacer upgrade.
- Ejecutar las instalaciones desde el command prompt = cmd desde la terminal de Visual Studio Code
# # CONSOLA PARA COMANDOS OMR - SQL
- Haremos uso de la sub consola de Python desde una terminal para acceder a la sub consola, para entrar usaremos "python" (solo funciona si hay un entorno virtual)
- Colocar el comando "from app import app", siendo app el nombre del directorio principal del proyecto
- Haremos el mismo comando de import pero en vez de la última app colocaremos el "db", siendo "from app import db"
- Colocaremos las importaciones de las tablas, con el comando "from app import Cliente" siendo Cliente el nombre de la tabla o el nombre de la clase en el main.
- Para realizar transacciones de base de datos para el directorio, usamos "app.app_context().push()" para poder ejecutar dichas transacciones
- Finalmente crearemos un registro para la tabla cliente creando un objeto de la clase Cliente, con la siguiente estructura.
- - c = Cliente(username = "Andres", password = "1234", email = "andresfyatem@gmail.com") - donde se definen de una vez los datos del objeto para cada una de sus columnas.
- - Los valores pueden cambiar según la tabla
- Añadimos el objeto, invocando un metodo de la importación "db" anterior, con el comando "db.session.add(c)" siendo c el objeto que creamos antes
- El comando para poder insertar es el comando "db.session.commit()", luego debemos verificar en la base de datos
# # # OTROS COMANDOS OMR
- Para **eliminar** un registro realizado en la base de datos, hacemos lo siguiente.
- - Debemos tener creado un objeto con los datos ya establecidos en el mismo y registrarlos.
- Para eliminarlos, hacemos uso del comando "db.session.delete(c)" siendo c el objeto de Cliente creado.
- Finalmente se usa el commit.
- Para **consultar** un dato en especifico, debemos hacer lo siguiente.
- - Creamos un objeto por ejemplo c1, a c1 le damos la siguiente estructura "c1 = Cliente.query.get(2)"
- - Donde Cliente es el nombre de la clase importada, query es la consulta a realizar, y get es donde solicitamos, en este caso, el id del cliente.
- Para **consultar** todos los datos de una tabla haremos lo siguiente.
- - crearemos un objeto ya sea "clientes" en donde almacenaremos lo siguiente "Cliente.query.all()" siendo Cliente la clase importada y all siendo la condicion de traer todo.
- Para **actualizar** un cliente, tomaremos el objeto que previamente se consulto (c1) y cambiaremos sus datos de la siguiente manera
- - c1.username = "Jhon Doe"
- - siendo "username" el campo de la tabla del objeto
- Debemos volver a usar el commit tras cada cambio o consulta

# # DEPENDENCIAS 
- pip install flask-wtf (formularios)

# # COMANDOS
- pip freeze > requirements.txt (para almacenar todas las dependencias necesarias en un txt)