CREATE TABLE `niveles` (
  `id` serial PRIMARY KEY,
  `numero` int,
  `descripcion` text
);

CREATE TABLE `secciones` (
  `id` serial PRIMARY KEY,
  `nombre` text,
  `alumnos` int,
  `nivel_id` int,
  `maestro_id` int
);

CREATE TABLE `maestros` (
  `id` serial PRIMARY KEY,
  `nombre` text,
  `apellidos` text,
  `correo` text,
  `direccion` text
);

ALTER TABLE `secciones` ADD FOREIGN KEY (`nivel_id`) REFERENCES `niveles` (`id`);

ALTER TABLE `secciones` ADD FOREIGN KEY (`maestro_id`) REFERENCES `maestros` (`id`);
