
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 큐
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K= Integer.parseInt(st.nextToken());
        Queue<Integer> queue = new LinkedList<>();

        for(int i=1; i<=N; i++) {
            queue.offer(i);
        }
        StringBuilder sb = new StringBuilder("<");
        while(queue.size() > 1 ) {
            for(int i=1; i<K; i++) {            // 0,1,2
                queue.offer(queue.poll());
            }
            sb.append(queue.poll());
            sb.append(", ");
        }
        if(queue.size() == 1) {
            sb.append(queue.poll());
        }
        sb.append(">");
        System.out.println(sb);
    }
}