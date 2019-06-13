package com.euler.defaultpackage;


public class Euler092 {

    public static void main(String[] args) {

        /*
        * Brute Force
        * */
//        int counter = 0;
//        for (int number = 2; number < 10000000; ++number) {
//            int temp;
//            int t = number;
//            while (true) {
//                temp = digitSquareSum(t);
//                if (temp == 1) {
//                    break;
//                }
//
//                if (temp == 89) {
//                    counter += 1;
//                    System.out.println(number);
//                    break;
//                }
//                t = temp;
//            }
//        }
//        System.out.println(counter);

        /*
         * Faster Brute Force using cache
         */
        int counter = 0;
        int target = 10000000;
        int cacheSize = (int)(81 * Math.log10(target));
        boolean[] cache = new boolean[cacheSize + 1];
        for(int i = 2; i <= cacheSize; ++i){
            int next = digitSquareSum(i);
            while(next > i && next != 89){
                next = digitSquareSum(next);
            }
            if(cache[next] || next == 89){
                cache[i] = true;
                counter++;
            }
        }
        for(int i = cacheSize + 1; i < target; ++i){
            if(cache[digitSquareSum(i)]){
                ++counter;
            }
        }
        System.out.println(counter);
    }

    public static int digitSquareSum(long n) {

        int total = 0;
        String num = String.valueOf(n);
        char[] numArray = num.toCharArray();
        for (char i : numArray) {
            total += Math.pow(Long.parseLong(String.valueOf(i)), 2);
        }
        return total;
    }

}
