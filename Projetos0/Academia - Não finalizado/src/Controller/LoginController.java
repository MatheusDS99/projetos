/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controller;

import view.Login;

/**
 *
 * @author Matheus
 */
public class LoginController {

    private final Login view;

    
    
    
    
    
    public LoginController(Login view) {
        this.view = view;
        
    }
    
    public void entrarNoSistema(){
        
    }
    
    
    
    public void Tarefa() {
        
        System.out.println("Busquei algo do banco de dados.");
        this.view.exibeMensagem("Executei a tarefa");
        
    }
    
}
