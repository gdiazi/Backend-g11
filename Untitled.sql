CREATE TYPE "tipo_usuario" AS ENUM (
  'CLIENTE',
  'ADMINISTRADOR'
);

CREATE TABLE "productos" (
  "id" serial PRIMARY KEY,
  "nombre" text,
  "precio" float,
  "precio_oferta" float,
  "disponible" boolean,
  "descripcion" text,
  "procedencia" text
);

CREATE TABLE "usuarios" (
  "id" serial PRIMARY KEY,
  "nombre" text,
  "apellido" text,
  "correo" text UNIQUE,
  "password" text,
  "tipo_usuario" tipo_usuario
);

CREATE TABLE "carrito" (
  "id" serial PRIMARY KEY,
  "usuario_id" int
);

CREATE TABLE "ItemsCarrito" (
  "id" int PRIMARY KEY,
  "cantidad" int,
  "producto_id" int,
  "carrito_id" int
);

ALTER TABLE "carrito" ADD FOREIGN KEY ("usuario_id") REFERENCES "usuarios" ("id");

ALTER TABLE "ItemsCarrito" ADD FOREIGN KEY ("carrito_id") REFERENCES "carrito" ("id");

ALTER TABLE "ItemsCarrito" ADD FOREIGN KEY ("producto_id") REFERENCES "productos" ("id");
