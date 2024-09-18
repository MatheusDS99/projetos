/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package view;

import view.models.Cliente;
import view.models.Pessoa;
import view.models.Usuario;

/**
 *
 * @author Matheus
 */
public class Main {
    public static void main (String [] args){
        
        
        Cliente cliente = new Cliente(2, "Thiago", "Rua teste", "000001");
        System.out.println(cliente.getNome());
        Usuario usuario = new Usuario("100", 2, "thiago");
        System.out.println(usuario.getSenha());
        
    }
    
}
