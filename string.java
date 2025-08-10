public class string {
    public static void main(String[] argv) {
        /*
            char -> charector 'a'

            char[] -> char array -> string

            Java
            String Class -> [Data + Methods]
        */
        String a = "STUDENT"; // STUDENT -> S - T - U - D - E - N - T
        String []b = a.split("");
        String []k = { " # ", " * ", " - "};

        for(int i = 0; i < 15; i++) {
            String c = String.join(k[i % 3], b);
            System.out.println(c);
        }
        

        /*

        0 <- Exact Match
        -ve <- Second Word is largest
        +ve <- First word is largest

        */
    }
}