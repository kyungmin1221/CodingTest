import java.io.*;
import java.util.*;

public class Main {
    static int n,k;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        Queue<Integer> queue = new LinkedList<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());   // 시작위치
        k = Integer.parseInt(st.nextToken());   // 목표위치
        visited = new boolean[100001];
        visited[n] = true;
        queue.add(n);

        int count = 0;

        while(true) {
            if( n == k) {
                System.out.println(0);
                return;
            }
            int size = queue.size();
            count ++;
            for(int i=0; i<size; i++) {
                int poll = queue.poll();
                visited[poll] = true;
                if(poll - 1 == k || poll + 1 == k || poll * 2 == k) {
                    System.out.println(count);
                    return;
                }
                if(poll - 1 >= 0 && !visited[poll-1]) {
                    visited[poll-1] = true;
                    queue.add(poll-1);
                }
                if(poll + 1 <= 100000 && !visited[poll+1]) {
                    visited[poll+1] = true;
                    queue.add(poll+1);
                }
                if(poll*2 <= 100000 && !visited[poll*2]) {
                    visited[poll*2] = true;
                    queue.add(poll*2);
                }
            }
        }
    }
}