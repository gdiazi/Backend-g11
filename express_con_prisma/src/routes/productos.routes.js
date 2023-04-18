import { Router} from "express";
import { crearProducto, devolverProducto, listarProductos, actualizarProducto } from "../controllers/productos.controllers.js";

export const productoRouter = Router();

productoRouter.post("/productos", crearProducto);

productoRouter.get("/producto/:id", devolverProducto);

productoRouter.get("/productos", listarProductos);

productoRouter.put("/producto/:id", actualizarProducto);
