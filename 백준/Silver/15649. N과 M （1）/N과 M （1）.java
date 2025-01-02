import java.util.*;
import java.io.*;


public class Main {
    static int n,m ;
    static boolean[] visited;
    static int[] box;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException{
        BufferedReader br = new  BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        visited = new boolean[n+1];
        box = new int[m];

        nAndM(0);
        System.out.println(sb);
    }

    private static void nAndM(int index) {
        if(index == m ) {
            for(int i=0; i<m; i++) {
                sb.append(box[i]+" ");
            }
            sb.append("\n");
            return;
        }

        for(int i=1; i<=n; i++) {
            if(visited[i]) {
                continue;
            }
            visited[i] = true;
            box[index] = i;
            nAndM(index + 1);
            visited[i] = false;
        }
    }
}