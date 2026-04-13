class Solution {
    public long solution(long n) {
        long answer = 0;
        
        double checkNum =  Math.sqrt(n);
        if( checkNum % 1 == 0) { 
            // 제곱근 
            answer = (long) Math.pow(checkNum + 1,2);
           
        }  else { 
            answer = -1;
        }
        
        return answer;
    }
}