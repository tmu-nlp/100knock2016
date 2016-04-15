/*
 * Chapter01, knock01
 * Task: String slicing stride.
 */

using System;


public class SliceString {
    static public void Main() {
        string word = "パタトクカシーー";
        Console.WriteLine(slice(word, 0, 2));
    }

    public static string slice(string str, int start=0, int stride=1) {
        string concat_string = "";
        for (int i=start; i < str.Length; i += stride) {
            concat_string += str[i];
        }

        return concat_string;
    }

}

