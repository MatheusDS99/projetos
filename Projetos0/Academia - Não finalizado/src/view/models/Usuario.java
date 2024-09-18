/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package view.models;

import java.util.Date;

/**
 *
 * @author Matheus
 */
public class Usuario extends Pessoa {
    
    
    protected String senha;
    protected String nivelAcesso;

    public Usuario(String senha, int Id, String nome) {
        super(Id, nome);
        this.senha = senha;
    }

    public Usuario(String senha, String nivelAcesso, int Id, String nome, char sexo, String dataNascimento, String telefone, String email, String rg) {
        super(Id, nome, sexo, dataNascimento, telefone, email, rg);
        this.senha = senha;
        this.nivelAcesso = nivelAcesso;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getNivelAcesso() {
        return nivelAcesso;
    }

    public void setNivelAcesso(String nivelAcesso) {
        this.nivelAcesso = nivelAcesso;
    }
 

   
    
    
}
