/*
 * Chapter01, knock01
 * Task: String slicing stride.
 */

using System;


public class SliceString {
    static public void Main() {
        string word = "パタトクカシーー";
        Console.WriteLine(Slice(word, 0, 2));
    }


    public static string Slice(string str, int start=0, int stride=1) {
        string concatString = "";
        for (int i=start; i < str.Length; i += stride) {
            concatString += str[i];
        }
        return concatString;
    }
}

