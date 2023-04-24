import { Router} from "express";
import * as controller from "../controllers/eventos.controllers.js";

import { validarToken } from '../utils/wachiman.js';


export const eventoRouter = Router();


//eventoRouter.post('/eventos', validarToken, controller.crearEvento);
//eventoRouter.route("/eventos").post(controller.crearEvento);

eventoRouter.route("/eventos").post(validarToken, controller.crearEvento);

eventoRouter.route("/prueba").get(controller.probarS3);