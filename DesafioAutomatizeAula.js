// Função principal
function concluirAulas() {
  // Pergunta ao usuário quantas aulas deseja concluir
  const numAulas = parseInt(prompt("Quantas aulas deseja concluir?"), 10);

  if (isNaN(numAulas) || numAulas <= 0) {
    alert("Por favor, insira um número válido de aulas.");
    return;
  }

  let aulasConcluidasComSucesso = 0;

  function clicarBotao() {
    const botao = Array.from(document.querySelectorAll('button[type="submit"]'))
      .find(btn => btn.textContent.includes('Concluir aula'));
    
    if (botao) {
      console.log('Botão encontrado');
      botao.click();
      console.log('Botão clicado');
      
      function esperarEClicarNovamente(tentativas = 0, maxTentativas = 30) {
        if (tentativas >= maxTentativas) {
          console.log('Número máximo de tentativas atingido. Botão não encontrado.');
          proximaAula();
          return;
        }

        if (document.readyState === 'complete') {
          setTimeout(() => {
            const novoBotao = Array.from(document.querySelectorAll('button[type="submit"]'))
              .find(btn => btn.textContent.includes('Concluir aula'));
            
            if (novoBotao) {
              novoBotao.click();
              console.log('Botão clicado novamente após carregamento da página e espera');
              aulasConcluidasComSucesso++;
              console.log(`Aulas concluídas com sucesso: ${aulasConcluidasComSucesso}`);
              proximaAula();
            } else {
              console.log('Botão não encontrado. Tentando novamente...');
              setTimeout(() => esperarEClicarNovamente(tentativas + 1), 1000);
            }
          }, 1000);
        } else {
          setTimeout(() => esperarEClicarNovamente(tentativas), 100);
        }
      }

      esperarEClicarNovamente();
    } else {
      console.log('Botão não encontrado inicialmente');
      proximaAula();
    }
  }

  function proximaAula() {
    if (aulasConcluidasComSucesso < numAulas) {
      setTimeout(clicarBotao, 2000); // Espera 2 segundos antes de tentar a próxima aula
    } else {
      alert(`Concluído! ${aulasConcluidasComSucesso} aulas foram marcadas como concluídas.`);
    }
  }

  clicarBotao();
}

// Inicia o processo
concluirAulas();
