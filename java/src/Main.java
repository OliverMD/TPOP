import java.util.Scanner;
import java.util.Arrays;
import java.util.GregorianCalendar;

public class Main {

    public static void main(String[] args) {
        //bmrCalculator();
        while (true) {
        }
    }

    public static void bmrCalculator(){
        System.out.println("###Welcome to the BMR Calculator! ###");
        Scanner input = new Scanner(System.in);
        System.out.print("Please enter your weight in pounds: ");
        String weightStr = input.next();
        float weight = Float.parseFloat(weightStr);
        System.out.print("Please enter your height in inches: ");
        float height = Float.parseFloat(input.next());
        System.out.print("Please enter your age in years: ");
        float age = Float.parseFloat(input.next());
        System.out.printf("You can eat %.2f chocolate bars if you are a woman!\n", (655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)) / 230);
        System.out.printf("You can eat %.2f chocolate bars if you are a man!", (66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)) / 230);
        return;

    }

    /**
     * Checks whether a given input is a valid palindrome.
     */
    public static void palindrome(){
        Scanner input = new Scanner(System.in);
        System.out.print("Please enter the word:");
        String word = input.next();
        char[] wordArray = word.toCharArray();
        for(int i = 0; i < Math.floor(word.length()/2); i++){
            if (wordArray[i] != wordArray[word.length() - i -1]){
                System.out.println("Not a palindrome!");
                return;
            }
        }

        System.out.println("It's a palindrome!");
    }

}
