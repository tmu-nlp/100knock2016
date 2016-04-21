/*
 * Chapter01, knock02
 * Task: concat two strings alternately
 */

using System;


public class ConcatString {
    static public void Main() {
        string word1 = "パトカー";
        string word2 = "タクシー";
        Console.WriteLine(Concat(word1, word2));
    }


    public static string Concat(string str1, string str2) {
        string concatString = "";
        for (int i=0; i < System.Math.Max(str1.Length, str2.Length); i ++) {
            concatString += str1[i];
            concatString += str2[i];
        }
        return concatString;
    }
}

