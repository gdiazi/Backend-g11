import { Router} from "express";
import { crearProducto, devolverProducto } from "../controllers/productos.controllers.js";

export const productoRouter = Router();

productoRouter.post("/productos", crearProducto);

productoRouter.get("/producto/:id", devolverProducto);