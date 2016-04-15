/*
 * Chapter01, knock04
 * Task: make map
 */

using System;
using System.Collections.Generic;

public class ElementMap {
    static public void Main() {
        string sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.";
        PrintMap(MakeMap(sentence));
    }


    public static Dictionary<string, int> MakeMap(string str) {
        string[] delimiter= new string[] {" "};
        string[] words = str.Split(delimiter, StringSplitOptions.None);
        Dictionary<string, int> elementMap = new Dictionary<string, int>();
        int[] nums = new int[]{1, 5, 6, 7, 8, 9, 15, 16, 19, -1};
        int j = 0, end = 0;
        for (int i=0; i < words.Length; i++) {
            if (nums[j] == i + 1) {
                end = 1;
                j++;
            } else {
                end = 2;
            }
            elementMap[words[i].Substring(0, end)] = i + 1;
        }
        return elementMap;
    }

    public static void PrintMap(Dictionary<string, int> map) {
        foreach (KeyValuePair<string, int> pair in map) {
            Console.WriteLine(string.Format("{0} \t {1}", pair.Key, pair.Value));
        }
    }

}

