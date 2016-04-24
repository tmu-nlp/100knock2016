/*
 * Chapter02, knock19
 * Task: sort by word frequency .
 *       Unix Command ``sort and uniq''
 */

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;

public class Knock17 {
    static public void Main(string[] args) {
        Dictionary<string, int> dict = ExtractColumn(args[0]);
        List<KeyValuePair<string, int>> kvps= dict.ToList();
        kvps.Sort((x, y) => y.Value.CompareTo(x.Value));
        foreach (KeyValuePair<string, int> kvp in kvps) {
            Console.WriteLine(string.Format("{0}\t{1}", kvp.Key, kvp.Value));
        }
    }

    public static Dictionary<string, int> ExtractColumn(string path, int col=0) {
        char [] deli = new char [] {'\t', '\n'};
        Dictionary<string, int> dict = new Dictionary<string, int>();

        using (StreamReader sr = File.OpenText(path)) {
            string line = "";
            while ((line = sr.ReadLine()) != null) {
                string [] split = line.Split(deli);
                if (!dict.ContainsKey(split[col])) { dict[split[col]] = 1; }
                else {dict[split[col]] += 1; }
            }
        }
        return dict;
    }
}

