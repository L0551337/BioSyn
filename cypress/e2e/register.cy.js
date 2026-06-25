describe('Teste de Registro', () => {
  it('Deve registrar um novo usuário', () => {
    cy.visit('http://localhost:5000/cadastro')
    cy.get('input[name="nome"]').type('novo_usuario')
    cy.get('input[name="email"]').type('email@teste.com')
    cy.get('input[name="senha"]').type('senha123')
    cy.get('button[type="submit"]').click()
    cy.contains('Cadastro realizado com sucesso')
  })
})
