
/**
 * Write a description of class test here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class test
{

    public static void scrambleOrRemove(List<String> wordList){
        for(int i = 0; i < wordList.size();i++){
            String temp = wordList.get(i);
            
            String temp2 = scrambleWord(temp);
            
            if (temp.equals(temp2)){
                
                wordList.remove(i);
                
            }
            else {
                wordList.set(i,temp2);
                i++;
            }
        }
        
        
        
   }
    
    public int findMinPartIndex()
        {
        int index;
        return index
        }
}