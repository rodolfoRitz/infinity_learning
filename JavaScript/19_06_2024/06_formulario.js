let escolhaUsuario;
let botaoEnviar;

botaoEnviar.addEventListener("click", () => {
  debugger;
  try {
    let usuario = escolhaUsuario.value;
    usuario.toLowerCase();
    console.log("Consegui Converter");
    console.log(usuario);
  } catch (erro) {
    console.log(erro);
  } finally {
    console.log("A tentativa de conversão foi concluída");
  }
});

// 1. Crie um bloco `try` que tenta executar um código que define uma
//    variável `x=10`. Adicione um bloco `catch` para capturar e exibir
//    erros no console.
try {
  let x = 10;
} catch (erro) {
  console.log("Consegui Converter");
  console.log(erro);
}

// 2. Modifique o exercício anterior para forçar um erro colocando para
//    imprimir no console uma variável não definida e verifique se o `catch`
//    captura o erro.

