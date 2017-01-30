import java.io.File;
import java.util.Arrays;
import java.util.Scanner;


public class Pr67 {
	
	public static int N=100;
	
	public static void main(String[] args){
		try{
			//System.out.println("Reading data from file");
			
	        Scanner scan = new Scanner(new File("data.txt"));
			int[][] Table = new int[N][N];			
			
			for(int i=0; i<N; i++){
				Arrays.fill(Table[i], -1);
				for(int j=0; j<=i; j++){
					Table[i][j] = scan.nextInt();
					//System.out.print(Table[i][j]+" ");
				}
				//System.out.println("");			
			}
			
			//System.out.println("Read data");
			
			for(int i=1; i<N; i++){
				for(int j=0; j<=i; j++){
					int n1=0,n2=0;
					if(j<=i){
						if(Table[i-1][j]!=-1){n1=Table[i-1][j];}
						if(j>0){n2=Table[i-1][j-1];}
					}
					
					Table[i][j] = Math.max(n1, n2)+Table[i][j];
				}
			}
			
			
			int max=0;
			for(int i=0; i<N; i++){
				if(Table[N-1][i]>max) max = Table[N-1][i];
			}
			
			System.out.println(max);
			
		} catch(Exception e){
			e.printStackTrace();
		}
	}

}
