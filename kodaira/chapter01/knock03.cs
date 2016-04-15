/*
 * Chapter01, knock03
 * Task: count each word length
 */

using System;


public class CountLength {
    static public void Main() {
        string sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.";
        Console.WriteLine(IntToString(Count(sentence)));
    }


    public static int[] Count(string str) {
        string[] delimiter= new string[] {" "};
        string[] words = str.Split(delimiter, StringSplitOptions.None);
        int[] nums = new int[words.Length];
        for (int i=0; i < words.Length; i++) {
            nums[i] = words[i].Length;
            if (System.Text.RegularExpressions.Regex.IsMatch(words[i], "[\\.,]")) {
                nums[i] -=1;
            }
        }
        return nums;
    }

    public static string IntToString(int[] nums) {
        string num_s = "";
        foreach (int num in nums) {
            num_s += num.ToString();
        }
        return num_s;
    }
}

