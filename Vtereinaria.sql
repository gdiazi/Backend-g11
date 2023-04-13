CREATE TYPE "SEXO_MASCOTA" AS ENUM (
  'MACHO',
  'HEMBRA'
);

CREATE TYPE "tipo_usuario" AS ENUM (
  'CLIENTE',
  'ADMINISTRADOR'
);

CREATE TABLE "mascotas" (
  "id" serial PRIMARY KEY,
  "nombre" text,
  "sexo" SEXO_MASCOTA,
  "fecha_nacimiento" datetime,
  "alergias" text,
  "foto" text,
  "cliente_id" int
);

CREATE TABLE "cabecera_ventas" (
  "id" serial PRIMARY KEY,
  "total" float,
  "fecha" datetime,
  "serie" text,
  "numero" text,
  "mascota_id" int
);

CREATE TABLE "detalle_ventas" (
  "id" serial PRIMARY KEY,
  "cantidad" int,
  "precio" float,
  "importe" float,
  "producto_id" int,
  "cabecera_venta_id" int
);

CREATE TABLE "productos" (
  "id" serial PRIMARY KEY,
  "nombre" text,
  "precio_unit" float,
  "disponibilidad" boolean
);

CREATE TABLE "usuarios" (
  "id" serial PRIMARY KEY,
  "nombre" text,
  "correo" text UNIQUE,
  "password" text,
  "tipo" tipo_usuario
);

ALTER TABLE "mascotas" ADD FOREIGN KEY ("cliente_id") REFERENCES "usuarios" ("id");

ALTER TABLE "cabecera_ventas" ADD FOREIGN KEY ("mascota_id") REFERENCES "mascotas" ("id");

ALTER TABLE "detalle_ventas" ADD FOREIGN KEY ("cabecera_venta_id") REFERENCES "cabecera_ventas" ("id");

ALTER TABLE "detalle_ventas" ADD FOREIGN KEY ("producto_id") REFERENCES "productos" ("id");
