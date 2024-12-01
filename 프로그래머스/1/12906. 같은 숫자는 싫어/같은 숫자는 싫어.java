import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        answer.add(arr[0]);
        for(int i=1; i<arr.length; i++) {    //  1 2 3 4 5 6
            if(arr[i] == arr[i-1]) {
                continue;
            } else {
                answer.add(arr[i]);
            }
        }
        int[] result = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
        }
        
        return result;
       
    }
}