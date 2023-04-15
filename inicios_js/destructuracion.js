const data = {
    nombre: "GUillermo",
    correo: "guillermo.diazipa@gmail.com",
    hobbies: [
        {
            nombre: "Ir al estadio",
            intensidad: "Normal",
        },
        {
            nombre: "Programar",
            intensidad: "Alta",
        },
    ],
};


const {nombre} = data;

const correo = "juanitoalimaña@gmail.com";

const correo_usuario = data.correo;

const { correo: nuevo_correo } = data;

const { hobbies, ...otro } = data;

console.log(nombre);
console.log(correo_usuario);
console.log(nuevo_correo);
console.log(otro);