import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int k = gcd(n,m);

        System.out.println(k);
        System.out.println( (n*m) / k );
    }

    private static int gcd(int n, int m) {
        if(n % m == 0) {
            return m;
        }
        return gcd(m, n % m);
    }
}