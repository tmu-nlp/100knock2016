/*
 * Chapter01, knock02
 * Task: concat two strings alternately
 */

using System;


public class ConcatString {
    static public void Main() {
        string word1 = "パトカー";
        string word2 = "タクシー";
        Console.WriteLine(concat(word1, word2));
    }

    public static string concat(string str1, string str2) {
        string concat_string = "";
        for (int i=0; i < System.Math.Max(str1.Length, str2.Length); i ++) {
            concat_string += str1[i];
            concat_string += str2[i];
        }
        return concat_string;
    }

}

