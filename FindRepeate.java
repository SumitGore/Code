public class FindRepeate {
    public static void main(String []argv) {
        // BIT Manupalation -> Find Repeated number.
        // Doing the XOR with any number twise repeate the bit so number can shows it is repeated number.
        int []arr = {1,2,5,3,4,6,5,8,7};
        int ans = 0;
        int a = arr.length;
        for(int i = 0; i < a; i++) {
            ans =ans ^ arr[i];
            System.out.println(arr[i] + " with XOR -> " + ans);
        }

        for(int i = 1; i < a ; i++) {
            ans =ans ^ i;
        }
        System.out.println("Answer: " + ans);
    }
}