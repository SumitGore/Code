// Inverse Count 

class ic {
    public static void main(String[] argv) {
        int []array = {1, 2, 3, 4};
		// Add your logic here
		int cnt = 0;
		for(int i = 0; i < array.length; i++) {
			for(int j = i + 1; j < array.length; j++) {
                if((array[i] > array[j]) && i < j) {
                    // System.out.println(array[i] + " " + array[j]);
                    cnt += 1;
                }
			}
		}
		
		System.out.println(cnt);
    }
}