import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder result = new StringBuilder(); 

        int tc = Integer.parseInt(br.readLine()); 
        for (int count = 0; count < tc; count++) {
            Map<Integer, Integer> hashMap = new HashMap<>();

            int n = Integer.parseInt(br.readLine());
            int[] note1 = new int[n];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                note1[i] = Integer.parseInt(st.nextToken());
            }

            int m = Integer.parseInt(br.readLine());
            int[] note2 = new int[m];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) {
                note2[i] = Integer.parseInt(st.nextToken());
            }

            for (int x : note1) {
                hashMap.put(x, hashMap.getOrDefault(x, 0) + 1);
            }

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < m; i++) {
                if (hashMap.containsKey(note2[i])) {
                    sb.append("1").append('\n');
                } else {
                    sb.append("0").append('\n');
                }
            }
            result.append(sb);
        }

        System.out.print(result);
    }
}
