class Solution {
    public int solution(int[][] signals) {
        int answer = 0;
        int maxTime = 1; 
        // 먼저 두 신호등의 최소공배수를 구한다음 , 
        for(int i=0; i< signals.length; i++) {
            int sum = signals[i][0] + signals[i][1] + signals[i][2]; 
            maxTime = lcm(maxTime, sum);    
        } 
        
        // 그 최소공배수(maxTime) 만큼 초를 돌려서 노란색이 나오면 멈추고 그 초를 반환 
        // 아니면 -1 을 반환하는 로직 작성 
        
        for(int t = 1; t <= maxTime; t++) {
            boolean check = true;
            for(int l = 0; l < signals.length; l++) {
                int green = signals[l][0];
                int yello = signals[l][1];
                int red   = signals[l][2];
                
                int sumLight = green + yello + red;
                
                // 현재 초에 위치한 좌표 
                int current = (t-1) % sumLight;
                
                if( !(green <= current && current < green + yello)) {
                    check = false;   
                }
            }    
            if(check) {
                return t;
            }
        } 
        return -1;
        
    
    }
    
    
    
    // 최대공약수
    public static int gcd(int num, int num2) {
        if( num % num2 == 0) {
            return num2; 
        }  else {
            return gcd(num2 , num % num2);
        }
    } 
    
    // 최소공배수
    public static int lcm(int num, int num2) {
        return num / gcd(num,num2) * num2 ;
    } 
    
}