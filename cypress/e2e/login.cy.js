describe('Teste de Login', () => {
  it('Deve carregar a página de login', () => {
    cy.visit('http://localhost:5000/login') 
    cy.contains('Login')
  })

  it('Deve falhar ao tentar login com credenciais inválidas', () => {
    cy.visit('http://localhost:5000/login')
    cy.get('input[name="nome"]').type('usuario_invalido')
    cy.get('input[name="senha"]').type('senha_errada')
    cy.get('button[type="submit"]').click()
    cy.contains('Nome ou senha incorretos') 
  })

  it('Deve logar com credenciais válidas', () => {
    cy.visit('http://localhost:5000/login')
    cy.get('input[name="nome"]').type('novo_usuario')
    cy.get('input[name="senha"]').type('senha123')
    cy.get('button[type="submit"]').click()
    cy.url().should('include', '/painel')
  })
})
