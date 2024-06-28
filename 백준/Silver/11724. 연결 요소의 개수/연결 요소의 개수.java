import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Integer>[] A;
    static boolean[] visited;
    static void dfs(int node) {
        if(visited[node]) {
            return;
        }
        visited[node] = true;
        for(int i : A[node]) {
            if(visited[i] == false) {
                dfs(i);
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());   // 노드 개수
        int E = Integer.parseInt(st.nextToken());   // 에지 개수
        A = new ArrayList[N+1];
        visited = new boolean[N+1];
        for(int i =1; i<N+1; i++) {
            A[i] = new ArrayList<>();
        }
        for(int i=0; i<E; i++) {
            st = new StringTokenizer(bf.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            A[u].add(v);
            A[v].add(u);
        }
        int count = 0;
        for(int i=1; i<N+1; i++) {
            if(!visited[i]) {
                count ++;
                dfs(i);
            }
        }
        System.out.println(count);
    }
}