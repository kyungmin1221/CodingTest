import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String note = br.readLine();
        String findWord = br.readLine();
        int count = 0;

        while (note.contains(findWord)) {
            note = note.replaceFirst(findWord,"-");
            count ++;
        }

        System.out.println(count);
    }
}