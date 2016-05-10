/*
 * Chapter03, knock20
 * Task: Open json file and find {'title' = 'イギリス'}
 */

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using System.IO.Compression;
using System.Net;
using System.Text;


public class Knock20 {
    static public void Main(string[] args) {
        ExtractTarget(args[0]);
    }

    public static void ExtractTarget(string path, string target="エジプト") {

        using (StreamReader sr = File.OpenText(path)) {
            string line = "";
            while ((line = sr.ReadLine()) != null) {
                //line = "\"title\": \"エジプト\"";
                string title = System.Text.RegularExpressions.Regex.Replace(
                    line, @".*""title"": ""(.*)"".*", "$1");
                if (title == target) {
                    string text = System.Text.RegularExpressions.Regex.Replace(
                        line, @".*""text"": ""(.*)"",.*", "$1");
                    using (StreamWriter sw = File.CreateText("./data/UK.txt")) {
                        sw.WriteLine(text.Replace("\\n", "\n"));
                    }
                }
            }
        }
    }
}

