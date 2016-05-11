/*
 * Chapter03, knock23
 * Task: Find line is described section name and print section level and section name
 */

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using System.IO.Compression;
using System.Net;
using System.Text;


public class Knock23 {
    static public void Main(string[] args) {
        ExtractTarget(args[0]);
    }

    public static void ExtractTarget(string path) {

        using (StreamReader sr = File.OpenText(path)) {
            string line = "";
            string pattern = @"(=+) (.*) =+$";
            while ((line = sr.ReadLine()) != null) {
                if (System.Text.RegularExpressions.Regex.IsMatch(line, pattern)) {
                    Console.WriteLine(String.Format("Level: {1}, Section Name: {0}", 
                                System.Text.RegularExpressions.Regex.Replace(line, pattern, "$2"), 
                                System.Text.RegularExpressions.Regex.Replace(line, pattern, "$1").Length - 1));
                }
            }
        }
    }
}

