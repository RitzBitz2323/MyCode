import java.util.ArrayList;
/**
 * Write a description of class eadsadasd here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Activities
{
    public int findMinPartIndex()
        {
        int index = 0;
        int temp = activitiesList.get(0).getNumParticipants();
        for(int i = 1; i < activitiesList.size; i++){
            if(activitiesList.get(i).getNumParticipants() <= temp){
            
                temp = activitiesList.get(i).getNumParticipants();
                index = i;
            }
        
        }
        }
    public Activity[] getLowestActivities(int n){
        Collections.sort(this);
        ArrayList<Activity> random = new ArrayList<Activity>(n);
        for(int i = 0; i < n; i++){
            random.add(this.get(i));
        
        }
        return random;
    }  
    public Activity[] getAllGroupActivities(){
     /**
      * - The program would have a specified private variable called groupvar which is 
      * the number of people that would be needed to be classified as a group. The program would 
      * have a public groupactivities array list to hold all group activities. There would than
      * be a private for loop iterating though the allactivities list and check each one to
      * see if they fit the groupvar criteria and if they did, they would be added to the group
      * activities array list
        
        
        
        */
    
    }
        
}
