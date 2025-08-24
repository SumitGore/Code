//Valid Anagram
//Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

//An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

public class angram {
    public static void main(String[] argv) {
        String s1 = "AKBCCCC";
        String s2 = "CACBCCK";
        int []dic1 = new int[26];
        int []dic2 = new int[26];
        for(int i = 0; i < 26; i++) {
            dic1[i] = 0;
            dic2[i] = 0;
        }
        for(int i = 0; i < s1.length(); i++) {
            dic1[((int)s1.charAt(i))%65] += 1;
            // System.out.println(((int)s1.charAt(i)) - 65);
        }
        for(int i = 0; i < s2.length(); i++) {
            dic2[((int)s2.charAt(i))%65] += 1;
        }

        for(int i = 0; i < 26; i++) {
            System.out.printf("%d ", dic1[i]);
        }
        System.out.println();
        for(int i = 0; i < 26; i++) {
            System.out.printf("%d ", dic2[i]);
        }

        boolean isAng = false;

        for(int i = 0; i < 26; i++) {
            if(dic1[i] != dic2[i]) {
                isAng = true;
                System.out.println("\nNot Angram");
            }
        }

        if(!isAng) {
            System.out.println("\nIs Angram");
        }
    }
}