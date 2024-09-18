/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package view.models;

import java.util.Date;
import view.models.Pessoa;


/**
 *
 * @author Matheus
 */
public class Cliente extends Pessoa {
    
    
    protected String endereco;
    protected String cep;

    public Cliente(String endereco, String cep, int Id, String nome, char sexo, String dataNascimento, String telefone, String email, String rg) {
        super(Id, nome, sexo, dataNascimento, telefone, email, rg);
        this.endereco = endereco;
        this.cep = cep;
    }

    public Cliente( int Id, String nome, String endereco, String cep) {
        super(Id, nome);
        this.endereco = endereco;
        this.cep = cep;
    }
    

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public String getCep() {
        return cep;
    }

    public void setCep(String cep) {
        this.cep = cep;
    }

      
  

   
    }

    
    
   


