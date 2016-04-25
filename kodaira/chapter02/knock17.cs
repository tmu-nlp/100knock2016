/*
 * Chapter02, knock17
 * Task: sort and uniq first column.
 *       Unix Command ``cut and uniq''
 */

using System;
using System.IO;
using System.Collections.Generic;

public class Knock17 {
    static public void Main(string[] args) {
        HashSet<string> set = ExtractColumn(args[0]);
        foreach (string s in set) {
            Console.WriteLine(s);
        }
    }

    public static HashSet<string> ExtractColumn(string path, int col=0) {
        char [] deli = new char [] {'\t', '\n'};
        HashSet<string> set = new HashSet<string>();

        using (StreamReader sr = File.OpenText(path)) {
            string line = "";
            while ((line = sr.ReadLine()) != null) {
                string [] split = line.Split(deli);
                set.Add(split[col]);
            }
        }
        return set;
    }
}

