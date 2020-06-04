import java.util.ArrayList;
/**
 * Write a description of class asdasdasd here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Secret
{
    public static String newLetter(String letter, String rule){
        int count = 0;
        String secret = "";
        if(letter == rule.substring(rule.length() -1, rule.length())){
            secret = rule.substring(0,1);
            return secret;
        }
        for(int i = 0; i < rule.length(); i++){
            if(!(letter == rule.substring(i,i+1))){
                count++;
            
            }
            else if(letter == rule.substring(i,i+1)){
                secret = rule.substring(i+1,i+2);
                return secret;
            }
        }
        if(count >= rule.length()){
            return letter;
        }
        return secret;
    
    }
    /**
     * In order to change it so you have the rule variable within the class, you would 
     * first need to create a private string variable called rule only accessed by this class.
     * The variable will be accessed by a getter and setter method, both public. The setter
     * method would be public void called setRule
     * and pass in a string of letters and set this.rule to the string passed in. The public
     * getter method called getRule would return rule;
     * 
       **/
    
    
}
