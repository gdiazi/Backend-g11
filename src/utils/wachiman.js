import jwt from 'jsonwebtoken';
import { UsuarioModel } from '../models/usuarios.model.js';


//import { UsuarioModel } from "../models/usuarios.model";

export const validarToken = (req, res, next) => {


    const authorizationHeader = req.headers.authorization;

    if (!authorizationHeader) {
        return res.status(401).json({ mensaje: 'No se proporcionó una token.' });
    }

    const token = authorizationHeader.split(' ')[1];

    try {
        const payload = jwt.verify(token, process.env.JWT_SECRET);


        const usuarioEncontrado = UsuarioModel.findById({ _id: payload.jti });
        console.log({ usuarioEncontrado })

        req.usuario = usuarioEncontrado;
        next();

    } catch (error) {
        return res.status(401).json({ mensaje: 'Token no válida.' });
    }



    // 1ra parte validar que hay el header de authorization
    // Validar que la token sea correcta
    // agregar al req.user la informacion del usuario de la token



}