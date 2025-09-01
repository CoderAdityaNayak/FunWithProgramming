// reads files (in this case java.txt file)
// assisted by Abhinandan
import java.io.BufferedReader;
import java.io.FileReader;

public class J5 {
    public static void main(String[] Args)throws Exception{
        BufferedReader ab=new BufferedReader(new FileReader("java.txt"));
        int n1=Integer.parseInt(ab.readLine());
        int n2=Integer.parseInt(ab.readLine());
        ab.close();
       System.err.println(n1+","+n2);
        
    }
}
