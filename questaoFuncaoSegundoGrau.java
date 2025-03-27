import java.util.Locale;
import java.util.Scanner;

public class questaoFuncaoSegundoGrau {
	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);

		System.out.print("Me diga o valor de ax²: ");
		double Ax2 = sc.nextDouble();
		
		System.out.print("Me diga o valor de bx: ");
		double Bx = sc.nextDouble();
		
		System.out.print("Me diga o valor de c: ");
		double C = sc.nextDouble();
		
		double Delta, X1, X2;
		Delta = Math.pow(Bx, 2) - (4*Ax2*C);
		if (Delta<=0) {
			System.out.print("A função não tem raízes reais!\n");
		}
		X1 = (-Bx + Math.sqrt(Delta)) / (2*Ax2);
		X2 = (-Bx - Math.sqrt(Delta)) / (2*Ax2);
		
		System.out.printf("X': %.2f\nX'': %.2f", X1, X2);
	}
}