/*
 * Chapter01, knock05
 * Task: get bigram
 */

using System;


public class Bigram {
    static public void Main() {
        string sentence = "I am an NLPer";
        // get word bigram
        PrintStrings(GetBigram(sentence));
        // get character bigram
        PrintStrings(GetBigram(sentence, ""));
        
    }


    public static string[] GetBigram(string str, string d=" ") {
        string[] delimiter= new string[] {d};
        var words = (d != "") ? str.Split(delimiter, StringSplitOptions.None) : new string[str.Length];
        if (words[0] == null) {
            for (int i=0; i < str.Length; i++) words[i] = str[i].ToString();
        }
        string[] bigram = new string[words.Length];
        for (int i=0; i < words.Length-1; i++) {
            bigram[i] = (String.Format("{0} {1}", words[i], words[i+1])); 
        }
        return bigram;
    }

    public static void PrintStrings(string[] strs) {
        foreach (string str in strs) {
            Console.WriteLine(str);
        }
    }
}

