/*
 * Chapter03, knock22
 * Task: Get line that include [[Category:****]] and print only ****
 */

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using System.IO.Compression;
using System.Net;
using System.Text;


public class Knock22 {
    static public void Main(string[] args) {
        ExtractTarget(args[0]);
    }

    public static void ExtractTarget(string path, string target="File:") {

        using (StreamReader sr = File.OpenText(path)) {
            string line = "";
            while ((line = sr.ReadLine()) != null) {
                if (System.Text.RegularExpressions.Regex.IsMatch(line, target)) {
                    Console.WriteLine(System.Text.RegularExpressions.Regex.Replace(line, @".*File:(.*?)\|.*", "$1"));
                    
                }
            }
        }
    }
}

