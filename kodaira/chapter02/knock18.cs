/*
 * Chapter02, knock18
 * Task: sort descending order.
 *       Unix Command ``sort''
 */

using System;
using System.IO;
using System.Collections.Generic;

public class Knock18 {
    static public void Main(string[] args) {
        string[] lines = Sort(args[0]);
        Console.WriteLine(string.Join("\n", lines));
    }

    public static string[] Sort(string path, int col=0) {
        char [] deli = new char [] {'\t', '\n'};
        var lines = new List<string []>();
        using (StreamReader sr = File.OpenText(path)) {
            string line = "";
            while ((line = sr.ReadLine()) != null) {
                lines.Add(line.Split(deli));
            }
        }

        int index = 0;
        String[] sortedLines = new String[lines.Count];
        lines.Sort((x, y) => float.Parse(x[2]).CompareTo(float.Parse(y[2])));
        
        foreach (string[] split in lines) {
            sortedLines[index++] = (string.Join(" ", split));
        }

        return sortedLines;
    }
}

