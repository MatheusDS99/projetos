package projetos.Projetos0.Calculadoras;

import java.util.Scanner;

public class CalculadoraSimples {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String escolha;
        
        do {
            // Exibe o menu
            System.out.println("Escolha a operação:");
            System.out.println("1. Adição");
            System.out.println("2. Subtração");
            System.out.println("3. Multiplicação");
            System.out.println("4. Divisão");
            System.out.println("5. Sair");

            escolha = scanner.nextLine();

            if (escolha.equals("5")) {
                System.out.println("Encerrando a calculadora.");
                break;
            }

            
            if (escolha.equals("1") || escolha.equals("2") || escolha.equals("3") || escolha.equals("4")) {
                System.out.print("Digite o primeiro número: ");
                double num1 = scanner.nextDouble();
                System.out.print("Digite o segundo número: ");
                double num2 = scanner.nextDouble();
                scanner.nextLine(); 

                double resultado;

                switch (escolha) {
                    case "1":
                        resultado = num1 + num2;
                        System.out.println("Resultado: " + num1 + " + " + num2 + " = " + resultado);
                        break;
                    case "2":
                        resultado = num1 - num2;
                        System.out.println("Resultado: " + num1 + " - " + num2 + " = " + resultado);
                        break;
                    case "3":
                        resultado = num1 * num2;
                        System.out.println("Resultado: " + num1 + " * " + num2 + " = " + resultado);
                        break;
                    case "4":
                        if (num2 != 0) {
                            resultado = num1 / num2;
                            System.out.println("Resultado: " + num1 + " / " + num2 + " = " + resultado);
                        } else {
                            System.out.println("Erro: Divisão por zero.");
                        }
                        break;
                    default:
                        System.out.println("Escolha inválida.");
                        break;
                }
            } else {
                System.out.println("Escolha inválida. Tente novamente.");
            }
        } while (true);

        scanner.close();
    }
}
