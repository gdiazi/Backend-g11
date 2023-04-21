/*
  Warnings:

  - You are about to drop the `Usuarios` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `carrito` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `itemsCarrito` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `producto` table. If the table is not empty, all the data it contains will be lost.

*/
-- CreateEnum
CREATE TYPE "TIPO_USUARIO" AS ENUM ('ADMIN', 'CLIENTE');

-- DropForeignKey
ALTER TABLE "carrito" DROP CONSTRAINT "carrito_usuarioId_fkey";

-- DropForeignKey
ALTER TABLE "itemsCarrito" DROP CONSTRAINT "itemsCarrito_carrito_id_fkey";

-- DropForeignKey
ALTER TABLE "itemsCarrito" DROP CONSTRAINT "itemsCarrito_producto_id_fkey";

-- DropTable
DROP TABLE "Usuarios";

-- DropTable
DROP TABLE "carrito";

-- DropTable
DROP TABLE "itemsCarrito";

-- DropTable
DROP TABLE "producto";

-- DropEnum
DROP TYPE "tipo";

-- CreateTable
CREATE TABLE "usuarios" (
    "id" SERIAL NOT NULL,
    "nombre" TEXT NOT NULL,
    "apellido" TEXT NOT NULL,
    "correo" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "tipo_usuario" "TIPO_USUARIO" NOT NULL DEFAULT 'CLIENTE',

    CONSTRAINT "usuarios_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "carritos" (
    "id" SERIAL NOT NULL,
    "usuario_id" INTEGER NOT NULL,

    CONSTRAINT "carritos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "productos" (
    "id" SERIAL NOT NULL,
    "nombre" TEXT NOT NULL,
    "precio" DOUBLE PRECISION NOT NULL,
    "precio_oferta" DOUBLE PRECISION NOT NULL,
    "disponible" BOOLEAN NOT NULL DEFAULT true,
    "descripcion" TEXT,
    "procedencia" TEXT NOT NULL,

    CONSTRAINT "productos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "items_carritos" (
    "id" SERIAL NOT NULL,
    "carrito_id" INTEGER NOT NULL,
    "producto_id" INTEGER NOT NULL,
    "cantidad" INTEGER NOT NULL,

    CONSTRAINT "items_carritos_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "usuarios_correo_key" ON "usuarios"("correo");

-- CreateIndex
CREATE UNIQUE INDEX "carritos_usuario_id_key" ON "carritos"("usuario_id");

-- AddForeignKey
ALTER TABLE "carritos" ADD CONSTRAINT "carritos_usuario_id_fkey" FOREIGN KEY ("usuario_id") REFERENCES "usuarios"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "items_carritos" ADD CONSTRAINT "items_carritos_carrito_id_fkey" FOREIGN KEY ("carrito_id") REFERENCES "carritos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "items_carritos" ADD CONSTRAINT "items_carritos_producto_id_fkey" FOREIGN KEY ("producto_id") REFERENCES "productos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
