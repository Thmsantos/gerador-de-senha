function GerarSenha(){
    return Math.random().toString(36).slice(6)
}

let Array_senhas =  Array.apply(null, Array(4)).map(GerarSenha)

console.log(Array_senhas)


