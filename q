[33mcommit da76267c8ae9fd0fc2677af5be833f3258830ded[m[33m ([m[1;36mHEAD -> [m[1;32mnuevosTemplates[m[33m)[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Sat Jun 8 20:53:04 2024 -0500

    (Diapositiva 12) -> Se crea la carpeta templates para almacenar los html, luego se enlaza la ruta de los enlaces y se llama al documento a traves de la vista

[33mcommit 3c7019be24ad8beaa4d5957020e5e3aaaa3e7d9d[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Sat Jun 8 20:22:26 2024 -0500

    (Diapositiva 11) -> Prueba para ver que tipo te argumento reciben las vistas, reciben el nombre del usuario junto con una solicitud get

[33mcommit d716b9b3af3ee0e8f15949567ef1706984eaf80f[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Sat Jun 8 20:19:56 2024 -0500

    (Diapositiva 10) -> Creando una nueva vista llamada anotherView y roteandola con el nombre another/

[33mcommit 895d3a07858e1080ed4a8cef43717f5d5d9731a4[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Sat Jun 8 20:17:33 2024 -0500

    (Diapositiva 9) -> Probando la urlConfig del proyecto para rotear nuevas vistas se prueba con another/

[33mcommit e0e99e76583b90c657f6a4839cec5f88b0587965[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Sat Jun 8 20:12:40 2024 -0500

    (Diapositiva 8) -> Agregando la vista inicio como url a la aplicacion lista contactos

[33mcommit 1bbd613c5f460537ea1b08ae8b31303e1baf272f[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Sat Jun 8 20:10:42 2024 -0500

    (Diapositiva 7) -> Crear la nueva app inicio, modificando INSTALLED_APPS de settings del proyecto para incluir la aplicacion y luego crear la respuesta http en python en inicio/views

[33mcommit 59ca56dfe5cc21d4295f928a3003ad509e5e0fc5[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Sat Jun 8 20:05:45 2024 -0500

    (Diapositiva 6 Pregunta) -> Agregando el campo obligatorio con blank=False, en consecuencia los elementos que afectarian a la base de datos son null=True, default=True, null=False y los que no afectan son blank=True y blank=False, esos solo afectan al formulario en la vista

[33mcommit e3839a8bb957df170d4f5ea5e78b677ad25be6e7[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Sat Jun 8 19:59:50 2024 -0500

    (Diapositiva 5) -> Se cambia el modelo Persona para incluir el campo booleano de donador)
    ;

[33mcommit 18705be938a80eeb8d4b995bca0e0705b4b4d802[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Sat Jun 8 19:51:16 2024 -0500

    (Diapositiva 4 Pregunta) -> Depende de los campos actualizados como en este caso se añadio uno similar los cambios no se perciben, se truncan. Sin embargo si se añaden nuevos atributos a la tabla tenemos que actualizarlos con el parametro Null=True para que al actualizar y hacer las migraciones se autocompleten con None

[33mcommit b9e5f4ff28899ad7b6f0675aceb9e95ffff13243[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Sat Jun 8 19:43:48 2024 -0500

    (Diapositiva 4) -> Se añade un nuevo campo a la tabla

[33mcommit 7b35c37036301ad38c93f59df156e9d257711828[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Sat Jun 8 19:39:57 2024 -0500

    (Diapositiva 4) -> Error, se elimino los py de migrate, lo que hacia imposible reconoces las migraciones para crear las tablas, corregido!

[33mcommit cb7b7f7db33a377305517c855a389a56a1a9ff8e[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Sat Jun 8 19:24:05 2024 -0500

    (Diapositiva 3) -> Se reinicia la tabla de datos y se cambian los tipos de datos mas apropiados para el campo, en vez de usar un textField se utiliza un CharField con longtud de 100 y un IntegerField para la edad

[33mcommit 04ee14508a1365e7cc45d4e6fc4252888dd14f16[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Thu May 30 17:32:34 2024 -0500

    (Diapositiva 15) -> Se agrega a una nueva persona a la base de datos a traves de la shell de python, se modifico la base de datos

[33mcommit cc7ba082c41998ce2865ee4bad2a930ccfd28b35[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Thu May 30 17:29:04 2024 -0500

    (Diapositiva 14) -> Se registra el modelo Persona a 'personas/admin.py'

[33mcommit 8f67cbbcbed072ded03fdd39c2a7579f7cd8c64a[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Thu May 30 17:26:11 2024 -0500

    (Diapositiva 13) -> Se crea un nuevo superusuario cuyo nombre es 'david' y la contraseña es '12345678'
    ;

[33mcommit 34eaaf5b10b6660e9e561efeecd67e503881c426[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Thu May 30 17:24:13 2024 -0500

    (Diapositiva 11) -> Se actualizan los cambios hechos y mediante migrate se informa al framework, se modifican los archivos de la base de datos y los relacionados a pycache

[33mcommit ad1d575bfcad4738b3d7194ab83912123441542a[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Thu May 30 17:22:04 2024 -0500

    Se añade la app personas a las rutas de INSTALLED_APPS de 'settings.py'

[33mcommit 0d4e6530c54a19c1c91263f890cd32bc6c024d09[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Thu May 30 17:20:50 2024 -0500

    (Diapositiva 11) -> creacion de la clase Persona, con los atributos: nombres, apellidos, edad

[33mcommit 92f3761844be20d81f4884499d080c57a021c0df[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Thu May 30 17:18:25 2024 -0500

    (Diapositiva 10) -> Creacion de la aplicacion 'personas' con las configuraciones base

[33mcommit a8a1cc81635c4c4fb003d634008664b62097c4a9[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Thu May 30 17:16:58 2024 -0500

    (Diapositiva 8) -> Migraciones realizadas para actualizar los cambios en el proyecto

[33mcommit 89e66939371ef41eea68b5135e786261267919fd[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Thu May 30 17:14:54 2024 -0500

    (Diapositiva 7) -> Actualizando la informacion de settings.py, el LANGUAGE_CODE y el TIME_ZONE

[33mcommit 19a7524c9902ee1b7090db802c7de596b89e0dfb[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Thu May 30 17:12:59 2024 -0500

    (Diapositiva 7) -> Creacion del ambiente virtual dentro del directorio src, luego se crea un nuevo proyecto 'listaContactos'

[33mcommit 050bf38f92d95ebcfa5e82a654db722a3ecd958f[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Thu May 30 17:07:40 2024 -0500

    (Diapositiva 4) -> Se crea el entorno virtual cuyo nombre es 'proyecto', se activa el entorno y se instala Django en este entorno.

[33mcommit 1935a06addd7d78e5b86cb1244b5991cf428b754[m
Author: dev1d123 <dhuamanio@unsa.edu.pe>
Date:   Thu May 30 17:00:29 2024 -0500

    Creacion del repositorio local, previamente se instalo pip y virtualenv
