import java.util.*;
public class Test

{ 
   public static void main(String[] args) 
   { 
      StringBuffer s1 = new StringBuffer("UPES"); 
      String s2 = "JAVA"; 
      s1.append(s2); 
      s1.substring(4); 
      int foundAt = s1.indexOf(s2); 
      System.out.println(foundAt); 

   }

}