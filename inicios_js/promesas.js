

async function ejecucion(){


console.log('Sumar');
console.log('Restar');


const promesa = new Promise((resolve, reject) =>{
    setTimeout(()=>{
    //    resolve("guardada en BD");
    reject(new Error("Error al guardar el registro en la BD"));
    }, 5000);
});


// promesa
// .then((respuesta) => {
//     console.log(respuesta);
// })
// .catch((error) => {
//     console.log(error);
// });


const respuesta = await promesa;

console.log(respuesta);

try{
    const respuesta = await promesa;
    console.log(respuesta);

} catch(error){
    console.error("Error al ejecutar la promesa");
    console.error(error.message);

}



console.log("Finalizo!");

}

ejecucion();