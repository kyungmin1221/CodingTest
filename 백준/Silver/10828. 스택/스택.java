import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();

        int inputSize = Integer.parseInt(br.readLine());

        for(int i=0; i<inputSize; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String stackIn = st.nextToken();

            if(stackIn.equals("push")) {
                int newToken = Integer.parseInt(st.nextToken());
                stack.push(newToken);
            } else if(stackIn.equals("pop")) {
                if(stack.isEmpty()) {
                    sb.append(-1).append("\n");
                } else {
                    sb.append(stack.pop()).append("\n");
                }
            } else if(stackIn.equals("size")) {
                sb.append(stack.size()).append("\n");
            } else if (stackIn.equals("empty")) {
                if(stack.isEmpty()) {
                    sb.append(1).append("\n");
                } else {
                    sb.append(0).append("\n");
                }
            } else { // 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
                if(stack.isEmpty()) {
                    sb.append(-1).append("\n");
                } else {
                    sb.append(stack.peek()).append("\n");
                }
            }
        }
        System.out.println(sb);
    }
}