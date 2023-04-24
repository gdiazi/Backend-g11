import { UsuarioModel } from "../models/usuarios.model.js";
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";



export const registroUsuario = async (req, res) => {
    const data = req.body;

    try {
        const nuevoUsuario = await UsuarioModel.create(data);

        console.log(nuevoUsuario);

        return res.status(201).json({
            message: "usuario creado exitosamente",
        });

    } catch (error) {
        return res.status(400).json({
            message: "error al crear usuario creado exitosamente",
            content: error.message,
        });

    }
};


export const loginUsuario = async (req, res) => {

    const { correo, password } = req.body

    try {
        const buscarUsuario = await UsuarioModel.findOne({ correo })

        console.log({ buscarUsuario })

        if (!buscarUsuario) {
            throw new Error('El usuario no existe')
        }

        const encontrarContraseña = bcrypt.compare(password, buscarUsuario.password)

        if (encontrarContraseña) {


            const token = jwt.sign({ userId: buscarUsuario.id }, process.env.JWT_SECRET, { expiresIn: '1h' });


            return res.json({ content: token })
        } else {
            throw new Error('Credenciales incorrectas')
        }
    } catch (error) {
        return res.status(400).json({
            message: 'Error al autenticar al usuario',
            content: error.message
        })
    }

}