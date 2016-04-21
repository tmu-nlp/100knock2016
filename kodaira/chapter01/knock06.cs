/*
 * Chapter01, knock06
 * Task: set
 */

using System;
using System.Collections.Generic;

using StrSet = System.Collections.Generic.HashSet<string>;


public class Set {
    static public void Main() {
        string word1 = "paraparaparadise";
        string word2 = "paragraph";

        // get character bigram
        StrSet set1 = (GetBigram(word1, ""));
        StrSet set2 = (GetBigram(word2, ""));
        StrSet union = new StrSet(set1);
        StrSet except = new StrSet(set1);
        StrSet intersect = new StrSet(set1);
        union.UnionWith(set2);
        except.ExceptWith(set2);
        intersect.IntersectWith(set2);
        Console.WriteLine("Set X:"); PrintStrings(set1);
        Console.WriteLine("Set Y:"); PrintStrings(set1);
        Console.WriteLine("Union X+Y:"); PrintStrings(union);
        Console.WriteLine("Except X-Y:"); PrintStrings(except);
        Console.WriteLine("Intersect X*Y:"); PrintStrings(intersect);

        Console.WriteLine();
        Console.WriteLine("`se' in Set X? -- {0}",  set1.Contains("se"));
        Console.WriteLine("`se' in Set Y? -- {0}",  set2.Contains("se"));
    }

    public static StrSet GetBigram(string str, string d=" ") {
        string[] delimiter= new string[] {d};
        StrSet bigram = new StrSet();

        var words = (d != "") ? str.Split(delimiter, StringSplitOptions.None) : new string[str.Length];
        if (words[0] == null) {
            for (int i=0; i < str.Length; i++) words[i] = str[i].ToString();
        }
        for (int i=0; i < words.Length-1; i++) {
            bigram.Add(String.Format("{0}{1}{2}", words[i], d, words[i+1]));
        }
        return bigram;
    }

    public static void PrintStrings(StrSet strset) {
        foreach (string one in strset)
            Console.Write("`{0}' ", one);
        Console.WriteLine();
    }

}

