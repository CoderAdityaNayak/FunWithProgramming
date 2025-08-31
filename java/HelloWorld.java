public class HelloWorld{
   public static void main(String[] Args){
      animal a= new animal(); 
      String name="Aditya";
      a.run(6);
     
      System.out.println("DOG");
      System.out.println("Hello");   // printing out a simple hello
      System.out.println(name.toUpperCase()); // converting to uppercase
      System.out.println(name.toLowerCase()); //converting to lowercase
      addExclamationPoint("HOTDOGS");
   } 
   public static void addExclamationPoint(String s){
      System.out.print(s+"!");   // simple function

   }
}
