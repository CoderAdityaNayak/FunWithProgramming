
import java.util.Scanner;

class S1{
    public static void main(String[] Arg){
        
        System.out.println("Please select the number of stars you want:");
        Scanner sc =new Scanner(System.in);
    // number of stars
        int s1=10; // no of space
        int s2=5; //reducing value for number of spaces
        int val =sc.nextInt();
        int val2=0;
        int n=1;
        float k=0;
        if(val>=10){
            val2=val/10;
            s1=s1+10+(val2*10);
        }
        if(val>=100){
            System.out.println("You will encounter this error because of space issue.");
        }
        while(n<(val+1)){
          for (float r = s1; r >s2-k ; r--){
              System.out.print(" ");
        }
        for(int i=0;i<n;i++){
            
            System.out.print("*");
            System.out.print(" ");
        }
        System.out.println(" ");
        n=n+1;
        k=k-(1);
       
    }
    sc.close();
        System.out.print("SPACE:"+(s1));
        if(val>=100){
            System.out.println("You will encounter this error because of space issue.");
        }
}

}
