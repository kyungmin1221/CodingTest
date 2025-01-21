import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());   // 9 (앨범 갯수)
        int m = Integer.parseInt(st.nextToken());   // 3 (담아야 하는 블루레이(박스)의 개수)
        int[] guitar = new int[n];

        int min = 0;
        int max = 0;

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            guitar[i] = Integer.parseInt(st.nextToken());
            if(min < guitar[i]) {
                min = guitar[i];
            }
            max = max + guitar[i];
        }

        while(min < max) {
            int mid = (min + max) / 2;
            int count = 0;
            int sum = 0;

            for(int i = 0; i < n; i++) {
                if(sum + guitar[i] > mid) {
                    count ++;
                    sum = 0;
                }
                sum += guitar[i];
            }
            if(sum != 0) {
                count ++;
            }

            if(count > m) {
                min = mid + 1;
            } else {
                max = mid;
            }
        }
        System.out.println(min);
    }
}