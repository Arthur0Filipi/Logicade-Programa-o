function validarFormulario(){

let titulo = document.getElementById("titulo").value
let ano = document.getElementById("ano").value
let paginas = document.getElementById("paginas").value

if(titulo == ""){
alert("Título obrigatório")
return false
}

if(isNaN(ano)){
alert("Ano deve ser número")
return false
}

if(paginas <= 0){
alert("Número de páginas deve ser maior que 0")
return false
}

return true
}