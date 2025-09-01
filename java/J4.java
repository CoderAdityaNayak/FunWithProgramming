// trying out "try"and"catch"
public class J4 {
    public static void main(String[] args) {
        
        System.out.println("Hello Bhai");
        

        try{
            int num=10/0;
            System.out.print("You are a boy");
        } catch (ArithmeticException e){
            System.out.println("You are a man");
        }
    }
}
