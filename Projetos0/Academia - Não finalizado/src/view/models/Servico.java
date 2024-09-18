/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package view.models;

/**
 *
 * @author Matheus
 */
public class Servico {
    
    private int Id;
    private String Descricao;
    private float Valor;

    public Servico(int Id, String Descricao, float Valor) {
        this.Id = Id;
        this.Descricao = Descricao;
        this.Valor = Valor;
    }

    public String getDescricao() {
        return Descricao;
    }

    public void setDescricao(String Descricao) {
        this.Descricao = Descricao;
    }

    public float getValor() {
        return Valor;
    }

    public void setValor(float Valor) {
        this.Valor = Valor;
    }
    
    
}
