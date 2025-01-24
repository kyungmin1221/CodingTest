import java.io.*;
import java.util.*;

public class Main {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int[] checkBox;
    static int flag = 0;
    private static int bfs(int z) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(z);
        visited[z] = true;

        while (!queue.isEmpty()) {
            int poll = queue.poll();

            for(int checkQueue : graph[poll]) {
                if(!visited[checkQueue]) {
                    visited[checkQueue] = true;
                    checkBox[checkQueue] = 1 - checkBox[poll];
                    queue.add(checkQueue);
                } else {
                    if(checkBox[poll] == checkBox[checkQueue]) {
                        flag = 1;   // 이분 그래프 만족 못하는 경우
                        return flag;
                    }
                }
            }
        }
        return flag;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int testCase = Integer.parseInt(st.nextToken());

        for(int i=0; i<testCase; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph = new ArrayList[u+1];
            visited = new boolean[u+1];
            checkBox = new int[u+1];
            for(int k=1; k<=u; k++) {
                graph[k] = new ArrayList<>();
            }
            for(int j=0; j<v; j++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                graph[a].add(b);
                graph[b].add(a);
            }
            for(int z =1; z<=u; z++)  {
                if(!visited[z]) {
                    bfs(z);
                }
            }
            if(flag == 1) {
                System.out.println("NO");
            } else {
                System.out.println("YES");
            }
            flag = 0;
        }
    }
}