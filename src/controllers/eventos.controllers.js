import { EventoModel } from "../models/eventos.model.js";
import { UsuarioModel } from "../models/usuarios.model.js";
import { subirImagenes } from "../utils/s3.js";

export const crearEvento = async (req, res) => {


    // ya nos vamos a recibir elk  usuario por el body,ahora el susuario vendra por el req.user
    const data = req.body;


    try{
        const nuevoEvento = await EventoModel.create(data);
        
        //reemplaza por req.user (usando autenticacion)
        //El findIf

        const usuarioEncontrado = await UsuarioModel.findById(data.usuario);

        await UsuarioModel.updateOne(
            { _id: data.usuario },
            {
                eventos: [ ...usuarioEncontrado.eventos, nuevoEvento._id],
            }
            
            )

        return res.status(201).json({
            message: "Evento creado",
            content: nuevoEvento,
        });

    }catch(error){

        return res.status(400).json({
            message: "Evento no creado",
            content: error.message
        });
    }
};


 export const probarS3 = async (req, res) => {
     const resultado = await subirImagenes("");
     console.log(resultado);

     res.json({
        message: "archivo subido",
     });
   };
