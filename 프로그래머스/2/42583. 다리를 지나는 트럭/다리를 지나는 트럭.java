import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int count = 0;
        int queueSum = 0;
        Queue<Integer> queue = new LinkedList<>();
        
        for(int truck : truck_weights) {
            while(true) {
                if(queue.size() == bridge_length) {
                    queueSum -= queue.remove();
                } 
                if(truck + queueSum <= weight) {
                    queue.add(truck);
                    queueSum += truck;
                    count ++;
                    break;
                } else {
                    queue.add(0);
                    count ++;
                }
            }
        }
        return count + bridge_length;
    }
}