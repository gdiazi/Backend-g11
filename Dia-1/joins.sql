INSERT INTO public.cursos (nombre, descripcion, habilitado) VALUES('CTA', 'Cienta Tecnologia y Ambiente', true);
INSERT INTO public.cursos (nombre, descripcion, habilitado) VALUES('Comunicacion', 'Letras', true);
INSERT INTO public.cursos (nombre, descripcion, habilitado) VALUES('Arte', 'Artes plasticas', false);
INSERT INTO cursos (nombre, descripcion, habilitado) VALUES('Ingles', 'English for kids', true);


SELECT * FROM public.alumnos INNER JOIN public.alumnos_cursos ON alumnos.id = alumnos_cursos.alumno_id;




SELECT * FROM
alumnos INNER JOIN alumnos_cursos
ON alumnos.id = alumnos_cursos.alumno_id
INNER JOIN cursos
ON alumnos_cursos.curso_id = cursos.id;


 SELECT * FROM
 alumnos AS a INNER JOIN alumnos_cursos AS ac
 ON a.id = ac.alumno_id
 INNER JOIN cursos AS c
 ON ac.curso_id = c.id;


SELECT nombre, apellido FROM alumnos AS a INNER JOIN alumnos_cursos AS ac
ON a.id = ac.alumno INNER JOIN cursos AS c ON ac.curso_id = c.id WHERE cursos.nombre = 'Comunicacion'


SELECT * FROM
alumnos INNER JOIN alumnos_cursos
ON alumnos.id = alumnos_cursos.alumno_id
INNER JOIN cursos
ON alumnos_cursos.curso_id = cursos.id
WHERE cursos.nombre='Comunicacion';
SELECT * FROM
alumnos INNER JOIN alumnos_cursos
ON alumnos.id = alumnos_cursos.alumno_id
INNER JOIN cursos
ON alumnos_cursos.curso_id = cursos.id
WHERE alumnos.nombre='Eduardo';
SELECT * FROM
alumnos INNER JOIN alumnos_cursos
ON alumnos.id = alumnos_cursos.alumno_id
INNER JOIN cursos
ON alumnos_cursos.curso_id = cursos.id
WHERE cursos.habilitado=true and alumnos.matriculado=true;