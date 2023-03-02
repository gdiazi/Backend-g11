---Para crear una base de datos
CREATE DATABASE pruebas;

--lista las base de datos en el servidor
 \l 

 -- nos cambia la bd que queremos

 \c
-- Se crea un enumerable que sirve para determinadas opciones
 CREATE TYPE tipo_sexo AS ENUM('MASCULINO', 'FEMENINO', 'PANSEXUAL', 'DONUTSEXUAL', 'OTRES');

-- sE CREA UNA TABVLEN LA BD
pruebas=# CREATE TABLE alumnos(
pruebas(# id SERIAL NOT NULL PRIMARY KEY,
pruebas(# nombre TEXT NOT NULL,
pruebas(# apellido VARCHAR(50),
pruebas(# sexo tipo_sexo DEFAULT 'OTRES',  -- SI UTILIZAMOS enum SE PUEDE UTILIZAR

pruebas(# fecha_creacion TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
pruebas(# matriculado BOOLEAN DEFAULT FALSE
pruebas(# );

--Mostrar todas las tablas
\dt
--mostrar detalle de la tabla


\d alumnos


mostrar la llave primaria de la tabla que es un indice
\d

-- para visualizar vaklires de un enum
SELECT enum_range(NULL::tipo_sexo)


pruebas=# INSERT INTO alumnos (nombre, apellido) VALUES
pruebas-#                     ('Juana', 'Martinez),
pruebas'#                     ('Robert', 'Juarez'),
pruebas'#                     ('Marigracia', 'Quispe');



pruebas=# INSERT INTO alumnos (id, nombre, apellido, sexo, fecha_creacion, matriculado) VALUES
pruebas-#                     (DEFAULT, 'Eduardo', 'de Rivero', 'MASCULINO', DEFAULT, true);
INSERT 0 1
pruebas=# INSERT INTO alumnos (nombre, apellido) VALUES
pruebas-#                     ('Juana', 'Martinez),
pruebas'#                     ('Robert', 'Juarez'),
pruebas'#                     ('Marigracia', 'Quispe');
pruebas'# INSERT INTO alumnos (nombre, apellido, sexo, matriculado) VALUES
pruebas'#                     ('Johana', 'Zuñiga', 'FEMENINO', false),
pruebas'#                     ('Martín', 'Zea', 'PANSEXUAL', false),
pruebas'#                     ('Roxana', 'Cutipo', 'DONASEXUAL', true);



pruebas=# SELECT * FROM alumnos WHERE sexo='MASCULINO';

pruebas=# SELECT * FROM alumnos WHERE sexo='MASCULINO' AND matriculado=true;


-- selecciona que todos tengan la letra o en cualquier parte
pruebas=# SELECT * FROM alumnos WHERE nombre LIKE '%o%';

--selecciona que en tercera posicion tenga letra o
pruebas=# SELECT * FROM alumnos WHERE nombre LIKE '__o%';

--selecc

---
SELECT * FROM alumnos WHERE nombre LIKE '__u%' OR nombre LIKE '__h%';

--selecciona todos los alumnos que tengan la letra x y sexo pansexual
 SELECT * FROM alumnos WHERE nombre LIKE '%x%' AND sexo='PANSEXUAL';


-- AQsi se xcrea una tabla con relacion entra la tabla alumnos y su columna id
pruebas=# CREATE TABLE direcciones(
pruebas(# id SERIAL PRIMARY KEY,
pruebas(# direccion TEXT,
pruebas(# numero INT,
pruebas(# referencia TEXT,
pruebas(# alumno_id INT,-- el tipo de dato tiene que ser el mismo que la otra columna sino dara error
pruebas(# CONSTRAINT fk_alumnos FOREIGN KEY(alumno_id) REFERENCES alumnos(id)
pruebas(# );
CREATE TABLE
pruebas=#
